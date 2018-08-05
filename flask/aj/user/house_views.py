import os

from flask import Blueprint, render_template, session, jsonify, request

from user.models import User, House, Area, Facility, HouseImage, Order

from utils import status_code
from utils.functions import is_login
from utils.settings import upload_folder

house_blueprint = Blueprint('house', __name__)


# 住房页面
@house_blueprint.route('/my_house/', methods=['GET'])
def my_house():
    return render_template('myhouse.html')


# 住房信息
@house_blueprint.route('/house_info/', methods=['GET'])
def house_info():
    user = User.query.filter(User.id == session['user_id']).first()
    if user.id_name:
        houses = House.query.filter(House.user_id == session['user_id']).order_by('-id')
        houses_list = [house.to_dict() for house in houses]
        return jsonify(code=status_code.OK, houses_list=houses_list)
    else:
        return jsonify(status_code.HOUSE_USERINFO_NAME_INVALID)


# 新房源
@house_blueprint.route('/newhouse/', methods=['GET'])
def new_house():
    return render_template('newhouse.html')


# 获取区域和家具
@house_blueprint.route('/area_facility/', methods=['GET'])
def area_facility():
    areas = Area.query.all()
    facilitys = Facility.query.all()

    areas_json = [area.to_dict() for area in areas]
    facilitys_json = [facility.to_dict() for facility in facilitys]

    return jsonify(code=status_code.OK, areas=areas_json, facilitys=facilitys_json)


# 新房源提交
@house_blueprint.route('/newhouse/', methods=['POST'])
@is_login
def my_newhouse():
    # 保存房屋信息，设施信息
    house_dict = request.form

    house = House()
    house.user_id = session['user_id']
    house.price = house_dict.get('price')
    house.title = house_dict.get('title')
    house.area_id = house_dict.get('area_id')
    house.address = house_dict.get('address')
    house.room_count = house_dict.get('room_count')
    house.acreage = house_dict.get('acreage')
    house.unit = house_dict.get('unit')
    house.capacity = house_dict.get('capacity')
    house.beds = house_dict.get('beds')
    house.deposit = house_dict.get('deposit')
    house.min_days = house_dict.get('min_days')
    house.max_days = house_dict.get('max_days')

    facilitys = house_dict.getlist('facility')
    for facility_id in facilitys:
        facility = Facility.query.get(facility_id)
        # 多对多关联
        house.facilities.append(facility)
    house.add_update()

    return jsonify(code=status_code.OK, house_id=house.id)


@house_blueprint.route('/house_images/', methods=['POST', 'GET'])
def house_images():
    house_id = request.form.get('house_id')
    house = House.query.filter(House.id == house_id).first()
    if house:
        img = request.files.get('house_image')
        save_url = os.path.join(upload_folder, img.filename)
        img.save(save_url)
        # 保存房屋和图片信息
        house_img = HouseImage()
        house_img.house_id = house_id
        img_url = os.path.join('upload', img.filename)
        house_img.url = img_url
        house_img.add_update()
        # 创建房屋首图
        if not house.index_image_url:
            house.index_image_url = img_url
            house.add_update()
        return jsonify(code=status_code.OK, img_url=img_url)


@house_blueprint.route('/detail/', methods=['GET'])
def detail():
    return render_template('detail.html')


@house_blueprint.route('/house_detail/<int:id>/', methods=['GET'])
def house_detail(id):
    house = House.query.get(id)
    return jsonify(code=status_code.OK, house=house.to_full_dict())


# 首页
@house_blueprint.route('/index/')
def index():
    return render_template('index.html')


# 给首页传值
@house_blueprint.route('/my_index/', methods=['GET'])
def my_index():
    # 首页需要图片和用户信息判断是否登录
    user_id = session['user_id']
    user = User.query.filter(User.id == user_id).first()
    user = user.to_auth_dict()

    if user:
        houses = House.query.filter(House.user_id == user_id).order_by(-House.id).all()[:3]
        houseinfo = [house.to_dict() for house in houses]

        return jsonify(code=status_code.OK, user=user, houseinfo=houseinfo)
    return jsonify(code=status_code.USER_LOGIN_PARAMS_INVALID)


@house_blueprint.route('/search/', methods=['GET'])
def search():
    return render_template('search.html')


@house_blueprint.route('/my_search/', methods=['GET'])
def my_search():
    # 区域id
    aid = request.args.get('aid')
    # 区域名称
    aname = request.args.get('aname')
    # 租房开始时间
    sd = request.args.get('sd')
    # 租房结束时间
    ed = request.args.get('ed')
    # 获取对应区域的房屋对象
    house = House.query.filter(House.area_id == aid)
    # 过滤登录用户发布房屋信息
    if 'user_id' in session:
        h_list = house.filter(House.user_id != session['user_id'])

    # 查询满足条件的房屋id
    order1 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= ed)
    order2 = Order.query.filter(Order.begin_date <= sd, Order.end_date >= sd)
    order3 = Order.query.filter(Order.begin_date >= sd, Order.begin_date <= ed)
    order4 = Order.query.filter(Order.begin_date >= sd, Order.end_date <= ed)
    house_ids1 = [order.house_id for order in order1]
    house_ids2 = [order.house_id for order in order2]
    house_ids3 = [order.house_id for order in order3]
    house_ids4 = [order.house_id for order in order4]

    house_ids = list(set(house_ids1 + house_ids2 + house_ids3 + house_ids4))
    # 最终房屋信息
    houses = h_list.filter(House.id.notin_(house_ids))

    house_dict = [house.to_dict() for house in houses]
    return jsonify(code=status_code.OK, house_dict=house_dict)

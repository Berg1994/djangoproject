OK = 200

# 请求成功
SUCCESS = {'code': 200, 'msg': '请求成功'}

# 数据库错误
DATABASE_ERROR = {'code': 500, 'msg': '数据库崩了'}

# 用于模块
USER_REGISTER_CODE_ERROR = {'code': 1000, 'msg': '验证码错误'}
USER_REGISTER_PARAMS_VALID = {'code': 1001, 'msg': '参数填写不完整'}
USER_REGISTER_MOBILE_INVALID = {'code': 1002, 'msg': '手机号码错误'}
USER_REGISTER_PASSWORD_ERROR = {'code': 1003, 'msg': '密码错误'}
USER_REGISTER_MOBILE_EXSIST = {'code': 1004, 'msg': '手机号已存在，请登录'}

# 用户登录
USER_LOGIN_PARAMS_INVALID = {'code': 1005, 'msg': '登录信息不完整'}
USER_LOGIN_PASSWORD_ERROR = {'code': 1006, 'msg': '密码错误'}
USER_LOGIN_PHTON_INVALID = {'code': 1007, 'msg': '手机号不正确'}
USER_LOGIN_PARMAS_VALID = {'code': 1008, 'msg': '登录信息不完整'}

# 用户设置
USER_SET_PARAMS_INVALID = {'code': 1009, 'msg': '信息填写不完整'}

USER_USERINOF_PORFILE_AVATAR_INVALID = {'code': 1010, 'msg': '图片格式错误'}

USER_USERINFO_NAME_EXSIST = {'code': 1011, 'msg': '用户名已存在'}

USER_USERINFO_ID_NAME_CARD_INVALID = {'code': 1012, 'msg': '请填写完整身份信息'}

USER_USERINFO_IDCARD_INVALID = {'code': 1013, 'msg': '身份证信息不正确'}

#房屋信息
HOUSE_USERINFO_NAME_INVALID = {'code':1014,'msg':'用户未实名认证'}
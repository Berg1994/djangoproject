from django.shortcuts import render


from rest_framework import mixins, viewsets

from stu.models import Student
from stu.stu_serializer import StuSerializer


def s_index(request):
    if request.method == 'GET':
        return render(request, 'student.html')


class StudentSource(mixins.ListModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.CreateModelMixin,
                    viewsets.GenericViewSet):

    #查询学生的数据 queryset 查询集
    queryset = Student.objects.all()
    #序列化
    serializer_class = StuSerializer



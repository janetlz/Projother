from django.core.paginator import Paginator
from django.http import HttpResponse
from django.shortcuts import render
from ProjOther import settings
from app01.models import User
from app01.models import Area


def index(request):

    return HttpResponse('显示首页')


def show_static(request):
    return render(request, 'show_static.html')


def add_user(request):
    return render(request, 'add_user.html')


def do_add_user(request):
    # todo: 获取上传的头像
    upload_file = request.FILES.get('avatar')

    # 判空
    if not upload_file:
        return render(request, 'add_user.html', {'errmsg': '请选择用户头像'})

    # todo: 保存用户的头像到硬盘中
    file_name = upload_file.name
    file_path = settings.MEDIA_ROOT + '/app01/' + file_name
    with open(file_path, 'wb') as file:
        for data in upload_file.chunks():
            file.write(data)

    # todo: 新增一个用户：保存用户名和用户上传的头像的路径到数据库中
    user = User()
    user.username = request.POST.get('username')
    user.avatar = 'app01/' + file_name
    user.save()
    return HttpResponse('新增成功')


def show_images(request):
    """显示所有用户的头像"""
    users = User.objects.all()
    context = {
        'users': users
    }
    return render(request, 'show_images.html', context)


def show_page(request, page_no):

    areas = Area.objects.filter(parent_id=1)

    paginator = Paginator(areas, 10)

    page = paginator.page(page_no)

    context = {
        'page': page
    }

    return render(request, 'show_page.html', context)


def select_area(request):
    provinces = Area.objects.filter(parent_id=1)
    context = {
        'provinces': provinces
    }
    return render(request, 'select_area.html', context)


def select_child(request, p_id):
    """
    获取下级地区数据
    :param request:
    :param p_id: 上级地区的id
    :return:
    """
    areas = Area.objects.filter(parent_id=1)

    areas_list = []  # areas是一个QuerySet的集合，以下循环会得到一个个Area的对象，不符合json的格式，所以需要一个list来操作
    for area in areas:
        areas_list.append([area.id, area.title])
    return None
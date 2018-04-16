from django.contrib import admin
from app01.models import User
from app01.models import Area


class AreaAdmin(admin.ModelAdmin):
    """模型管理类"""
    # 后台显示的字段
    list_display = ['id', 'title', 'parent_area']
    # 每页显示的条数
    list_per_page = 10
    # 操作栏的显示与隐藏
    actions_on_top = True
    actions_on_bottom = True

    # 搜索区域名称
    search_fields = ['title']
    # 要在编辑界面显示的字段
    fields = ['parent', 'title']

    # 分组显示 和 fields是互斥的，不能同时显示
    # fieldsets = (
    #     ('基本', {'fields': ('title',)}),
    #     ('基本', {'fields': ('parent',)}),
    # )


admin.site.register(Area, AreaAdmin)

admin.site.register(User)

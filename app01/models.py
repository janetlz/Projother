from django.db import models


class Area(models.Model):
    """地区类"""
    title = models.CharField(max_length=50, verbose_name='区域名称')

    parent = models.ForeignKey('self', null=True, blank=True)

    def parent_area(self):
        """获取上级区域"""

        if self.parent is None:
            return ''

        return self.parent.title

    def __str__(self):
        return self.title

    # 指定列的名字
    parent_area.short_description = '上级区域'
    # 排序条件
    parent_area.admin_order_field = 'id'


class User(models.Model):
    """用户名和头像模型"""
    # 用户名
    username = models.CharField(max_length=20)
    # upload_to: 表示图片要保存到 media/app01 子目录下
    # app01目录需要手动创建出来
    avatar = models.ImageField(upload_to='app01')

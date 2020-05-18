from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    mobile = models.CharField(max_length=11, unique=True)

    class Meta:
        db_table = 'novel_user'
        verbose_name = '用户表'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


# 小说类型
class Brand(models.Model):
    name = models.CharField(max_length=20, unique=True)

    class Meta:
        db_table = 't_brand'
        verbose_name = '小说类型'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 小说主体
class Novel(models.Model):
    STATUS = [
        [0, '连载中'],
        [1, '以完结']
    ]
    name = models.CharField(max_length=50, verbose_name='小说名')
    author = models.CharField(max_length=20, verbose_name='作者')
    icon = models.ImageField(upload_to='icon', verbose_name='图标')
    views = models.PositiveIntegerField('阅读量', default=0)
    brand = models.ForeignKey(to=Brand, on_delete=models.DO_NOTHING, related_name='novels')
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        db_table = 't_novel'
        verbose_name = '小说主体'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


# 小说章节
class Chapter(models.Model):
    title = models.CharField(max_length=50, verbose_name='章节标题')
    content = models.FileField(upload_to='content', verbose_name='内容')
    create_time = models.DateTimeField(auto_now=True, verbose_name='更新时间')
    novel = models.ForeignKey(to=Novel, on_delete=models.DO_NOTHING, related_name='chapters')

    class Meta:
        db_table = 't_chapter'
        verbose_name = '小说章节'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title

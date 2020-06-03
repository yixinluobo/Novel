from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from novel import serializers
from novel import models
from rest_framework.filters import SearchFilter, OrderingFilter
from utils import pangenations, throttles
from utils.response import APIResponse
from rest_framework_extensions.cache.decorators import cache_response
from rest_framework_extensions.cache.mixins import CacheResponseMixin


# 小说群查接口
class NovelListAPI(CacheResponseMixin, ListAPIView):  # 继承CacheResponseMixin实现缓存，且此类必须放在第一继承位
    queryset = models.Novel.objects.all()
    serializer_class = serializers.NovelModelSerializer

    # 过滤配置
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'author', 'status']
    ordering_fields = ['pk', 'views']
    # 分页
    pagination_class = pangenations.MyPageNumPagination


# 分类小说接口
class BrandListAPI(CacheResponseMixin, ListAPIView):
    # 访问频率限制
    throttle_classes = [throttles.SMSRateThrottle]

    queryset = models.Brand.objects.all()
    serializer_class = serializers.BrandModelSerializer

    # 过滤配置
    filter_backends = [SearchFilter]
    search_fields = ['name']
    # 分页
    pagination_class = pangenations.MyPageNumPagination


# 小说单查接口
class NovelAPIView(CacheResponseMixin, RetrieveAPIView):
    queryset = models.Novel.objects.all()
    serializer_class = serializers.NovelModelSerializer

    # 重写get方法，实现增加点击量
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        novel = models.Novel.objects.get(pk=pk)
        views = novel.views + 1
        novel.views = views
        novel.save()
        return self.retrieve(request, *args, **kwargs)


# 查看小说内容接口
class ChapterListAPIView(APIView):
    @cache_response()  # 针对非viewSet类使用此装饰器进行缓存
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        chapters = models.Chapter.objects.filter(novel=pk)
        # 创建分页对象
        paginate = pangenations.MyChapterPagination()
        page = paginate.paginate_queryset(chapters, request, view=self)
        chapters_ser = serializers.ChapterModelSerializers(page, many=True)
        return paginate.get_paginated_response(chapters_ser.data)

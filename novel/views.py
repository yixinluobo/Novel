from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework.views import APIView
from novel import serializers
from novel import models
from rest_framework.filters import SearchFilter, OrderingFilter
from utils import pangenations, throttles
from utils.response import APIResponse


# 小说群查接口


class NovelListAPI(ListAPIView):
    queryset = models.Novel.objects.all()
    serializer_class = serializers.NovelModelSerializer

    # 过滤配置
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ['name', 'author', 'status']
    ordering_fields = ['pk', 'views']
    # 分页
    pagination_class = pangenations.MyPageNumPagination


# 分类小说接口
class BrandListAPI(ListAPIView):
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
class NovelAPIView(RetrieveAPIView):
    queryset = models.Novel.objects.all()
    serializer_class = serializers.NovelModelSerializer


# 查看小说内容接口
class ChapterListAPIView(APIView):
    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        chapters = models.Chapter.objects.filter(novel=pk)
        # 创建分页对象
        paginate = pangenations.MyChapterPagination()
        page = paginate.paginate_queryset(chapters, request, view=self)
        chapters_ser = serializers.ChapterModelSerializers(page, many=True)
        return paginate.get_paginated_response(chapters_ser.data)
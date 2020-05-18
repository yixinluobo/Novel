from rest_framework.pagination import PageNumberPagination


class MyPageNumPagination(PageNumberPagination):
    page_query_param = 'page'
    page_size = 12
    page_size_query_param = 'page_size'
    max_page_size = 12


# 章节
class MyChapterPagination(PageNumberPagination):
    page_size = 1
    # 每页显示数据的数量
    max_page_size = 1
    # 每页最多可以显示的数据数量
    page_query_param = 'page'
    # 获取页码时用的参数
    page_size_query_param = 'page_size'
    # 调整每页显示数量的参数名

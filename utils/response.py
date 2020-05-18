from rest_framework.response import Response


# 自封装response
class APIResponse(Response):
    def __init__(self, data_status=0, data_msg='ok', results=None, http_status=None, headers=None, exception=False,
                 **kwargs):
        # data的初始状态
        data = {
            'status': data_status,
            'msg': data_msg,
        }
        # data响应数据体
        if results is not None:
            data['result'] = results
        # data响应其他内容
        data.update(kwargs)

        super().__init__(data=data, status=http_status, headers=headers, exception=exception)

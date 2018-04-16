from django.http import HttpResponse


class MyMiddleware(object):
    """自定义的中间件类"""

    def __init__(self):
        """服务器启动后，处理第一个请求时才会调用"""
        print('---init---')

    def process_request(self, request):
        """django创建request对象后，url匹配前调用"""
        print('---process_request---')

        # 禁止某ip访问网站
        # ip = request.META.get('REMOTE_ADDR')
        # if ip in['127.0.0.1']:  # 如果在黑名单中，则禁止访问
        #     return HttpResponse('禁止访问')

    def process_view(self, request, view_func, view_args, view_kwargs):
        """url匹配后，视图函数执行前调用"""
        print('---process_view---')

    def process_exception(self, request, exception):
        """试图函数执行出错时调用"""
        print('---process_exception')
        return HttpResponse('出错了： %s' % exception)

    def process_response(self, request, response):
        """视图函数执行后，返回内容给浏览器之前调用"""
        print('---process_response---')
        return response

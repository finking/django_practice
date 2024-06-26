

class AjaxMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.
        
        def is_ajax(self):
            return request.META.get(
                'HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

        request.is_ajax = is_ajax.__get__(request)
       
        response = self.get_response(request)

        # Code to be executed for each request/response after
        # the view is called.

        return response

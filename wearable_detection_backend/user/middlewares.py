from django.utils.deprecation import MiddlewareMixin


class DisableCSRFCheck(MiddlewareMixin):
    """
    关闭rest framwork的 CSRF
    """
    def process_request(self, request):
        setattr(request, '_dont_enforce_csrf_checks', True)

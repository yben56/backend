from core.i18n.resolver import resolve_language


class I18nMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        request.lang = resolve_language(request)
        return self.get_response(request)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from core.i18n.service import t


@api_view(['GET'])
def test(request):
    return Response({
        'error' : False,
        "code": "AUTH_INVALID_LOGIN",
        "message": t("AUTH_INVALID_LOGIN", request.lang),
        'data' : None
    }, status=status.HTTP_200_OK)
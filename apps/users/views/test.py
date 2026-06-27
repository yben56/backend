from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def test(request):
    return Response({
        'error' : False,
        'message' : '',
        'data' : None
    }, status=status.HTTP_200_OK)
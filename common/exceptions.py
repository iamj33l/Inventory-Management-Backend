from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import exception_handler


def custom_exception_handler(exception, context):

    response = exception_handler(exception, context)

    if response is None:
        response = Response({
            'detail': str(exception),
            'status_code': 500,
        }, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    return response
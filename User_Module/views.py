from django.http import HttpRequest
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token

from .serializers import LoginSerializer
from .models import UserModel


class LoginAPIView(APIView):
    """
    The Login API view to log in users with username and password
    """
    def post(self, request: HttpRequest, *args, **kwargs):
        """
        This method performs user login.
        param: request: HttpRequest
        return: HTTP response with user token
        """
        # validate entry data
        data = LoginSerializer(data=request.data)

        if not data.is_valid():
            return Response({'result': data.errors}, status=status.HTTP_400_BAD_REQUEST)

        # get username and password
        username = data.validated_data['username']
        password = data.validated_data['password']

        # check username
        user = UserModel.objects.filter(username=username).first()
        if user is None:
            return Response({'result': 'username or password is wrong'}, status=status.HTTP_404_NOT_FOUND)

        # check password
        if not user.check_password(password):
            return Response({'result': 'username or password is wrong'}, status=status.HTTP_404_NOT_FOUND)

        # delete old token
        Token.objects.filter(user=user).delete()

        # create new token
        token = Token.objects.create(user=user)

        # return user token
        return Response({'result': 'accept', 'token': token.key}, status=status.HTTP_200_OK)


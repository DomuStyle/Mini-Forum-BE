
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from .serializers import RegistrationSerializer



class RegistrationView(APIView):
    permission_classes = [AllowAny] # gives permission to use this view at any time

    def post(self, request):
        serializer = RegistrationSerializer(data=request.data)

        data = {}
        if serializer.is_valid():
            saved_account = serializer.save()
            token, created = Token.objects.get_or_create(user=saved_account) # get or create is used to make sure to get a token if it alrdy exists
            data = {
            'token': token.key,
            'username': saved_account.username,
            'email': saved_account.email,
            }

        else:
            data=serializer.errors

        return Response(data)
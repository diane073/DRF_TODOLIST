from rest_framework.views import APIView
from rest_framework import status
from rest_framework import permissions
from rest_framework.response import Response
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
)


class UserView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'가입완료'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
    
    @csrf_exempt
    def put(self, request):
        serializer = UserSerializer(data=request.data)
        user = request.data.get("email",None)  ## 수정
        print(request.user)
        print(user)

        if user == request.user:
            if serializer.is_valid():
                serializer.save()
                return Response({'message':'회원 정보 수정 완료'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':"권한이 없습니다"}, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.delete()
        return Response({'message':'회원 탈퇴 완료'}, status=status.HTTP_201_CREATED)



class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class mockView(APIView):
    permission_class = [permissions.IsAuthenticated]
    def get(self, request):
        user = request.user
        user.is_admin = True
        user.save()
        return Response('get 요청')




class LogoutView(APIView):
    def post(self, request):
        request.user.auth_token.delete()   #현재 access 토큰을 지워줌
        logout(request)
        return Response({'message': "Logout successful"})
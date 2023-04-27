from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from users.serializers import UserSerializer, CustomTokenObtainPairSerializer, UserProfileSerializer
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
    

class UserProfileView(APIView):
    def get(self, request, user_id):
        #login한 유저인지 먼저 확인
        user = get_object_or_404(CustomUser, id=user_id)
        print(user)
        print(request.user)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

    @csrf_exempt
    def put(self, request, user_id):
        user = get_object_or_404(CustomUser, id=user_id)  #user 데이터 가져와주기
        
        print(request.user)
        print(user)

        if user.id == request.user.id:  #요청유저와 유저데이터 id 일치 여부 검사
            if serializer.is_valid():
                serializer = UserProfileSerializer(user, data=request.data)
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':"권한이 없습니다"}, status=status.HTTP_403_FORBIDDEN)


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


class LogoutView(APIView):  #프론트 만들 것 아니면
    def post(self, request):
        request.user.access_token.delete()   #현재 access 토큰을 지워줌
        logout(request)
        return Response({'message': "Logout successful"})
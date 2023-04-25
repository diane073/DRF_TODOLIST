from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from todolists.serializers import ToDoListSerializer


# Create your views here.


class ToDoListView(APIView):
    def get(self, request):
        serializer = ToDoListSerializer(data=request.data)
    
    def post(self, request):
        serializer = ToDoListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'할일 작성 완료!'}, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class ToDoListDetailView(APIView):
    def put(self, request, todolist_id):
        pass
    
    def delete(self, request, todolist_id):
        pass
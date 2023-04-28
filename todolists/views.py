from rest_framework.views import APIView
from rest_framework import status, permissions
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from todolists.serializers import ToDoListSerializer, ToDoListCreateSerializer
from todolists.models import ToDoList
# Create your views here.


class ToDoListView(APIView):
    permission_class = [permissions.IsAuthenticated]

    def get(self, request):
        todolist = ToDoList.objects.filter(user=request.user).order_by('-created_date')
        serializer = ToDoListSerializer(todolist, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = ToDoListCreateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)


class ToDoListDetailView(APIView):
    def post(self, request, todolist_id): #할일 완료
        todo = get_object_or_404(ToDoList, id=todolist_id)
        if todo.is_completed == True:
            todo.update(completion_at = todo.completion_at)
            return Response(todo.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, todolist_id): #내용수정
        todo = get_object_or_404(ToDoList, id=todolist_id)
        if request.user == todo.user:
            serializer = ToDoListCreateSerializer(todo, data=request.data) #여기에 ㅅ

            if serializer.is_valid():
                serializer.save()
                return Response({'message':f'수정 완료! ${serializer.data}'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message':f'${serializer.errors}'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'message':'수정 권한이 없습니다!'}, status=status.HTTP_403_FORBIDDEN)


    def delete(self, request, todolist_id):
        todo = get_object_or_404(ToDoList, id=todolist_id)
        if request.user == todo.user:
            todo.delete()
            return Response("삭제되었습니다", status=status.HTTP_204_NO_CONTENT)
        else:
            return Response("권한이 없습니다", status=status.HTTP_403_FORBIDDEN)

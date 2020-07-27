from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from taskmanager.serializers import TaskSerializer, TaskSerializerForValidation, TaskSerializerValidation

# for the list class view
from rest_framework.pagination import PageNumberPagination
from rest_framework.generics import ListAPIView
from rest_framework.authentication import TokenAuthentication
from rest_framework.filters import SearchFilter


@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_task(request):
    account = request.user
    task_post = Task(author=account)
    serializer = TaskSerializerForValidation(task_post, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_task(request, description):
    try:
        task_post = Task.objects.get(description=description)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    return Response(TaskSerializer(task_post).data)


@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_task(request, description):
    try:
        task_post = Task.objects.get(description=description)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializerForValidation(task_post, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "The task '" + description + \
                        "' was successfully updated."
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes((IsAdminUser,))
def validate_task(request, description):
    try:
        task_post = Task.objects.get(description=description)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializerValidation(task_post, data=request.data)
    data = {}
    if serializer.is_valid():
        serializer.save()
        data["success"] = "The task '" + description + \
                        "' was successfully updated."
        return Response(data=data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_task(request, description):
    try:
        task_post = Task.objects.get(description=description)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    operation = task_post.delete()  
    data = {}
    if operation:
        data["success"] = "The task '" + description + \
                        "' was successfully deleted."
    else:
        data["failure"] = "delete failed"
    return Response(data=data)

# https://www.django-rest-framework.org/api-guide/filtering/
class ListTasks(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter,)
    search_fields = ('author__username', 'category', 'loc_geo')

    #The view's authentication class is explicitly set to TokenAuthentication only. It wont work with JWT token.
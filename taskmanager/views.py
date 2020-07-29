from django_filters.rest_framework import DjangoFilterBackend
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from taskmanager.serializers import (TaskSerializerBasicAccess,
                                     TaskSerializerFullAcess)

from .models import Task


@swagger_auto_schema(method='post', request_body=TaskSerializerFullAcess)
@api_view(['POST', ])
@permission_classes((IsAuthenticated,))
def create_task(request):
    task_post = Task(author=request.user)

    #TODO improve this section
    data_contains_state = False
    try:
        request.data['states']
        data_contains_state = True
    except:
        pass

    if not request.user.is_superuser and data_contains_state:
        return Response({'failed':'To post a state you must be a system admin.'}, 
                        status=status.HTTP_401_UNAUTHORIZED)
    elif request.user.is_superuser:
        serializer = TaskSerializerFullAcess(task_post, data=request.data)
    else:
        serializer = TaskSerializerBasicAccess(task_post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_task(request, pk):
    try:
        task_post = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'missing' : 'There is no task with the pk = ' + str(pk) + '.'},
                        status=status.HTTP_404_NOT_FOUND)
    return Response(TaskSerializerBasicAccess(task_post).data)


@swagger_auto_schema(method='put' , request_body=TaskSerializerFullAcess)
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_task(request, pk):
    try:
        task_post = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'missing' : 'There is no task with the pk = ' + str(pk) + '.'},
                        status=status.HTTP_404_NOT_FOUND)

    #TODO improve this section
    data_contains_state = False
    try:
        current_state = request.data['states']
        data_contains_state = True
    except:
        pass

    if not request.user.is_superuser and data_contains_state:
        return Response({'failed':'To validate a state you must be a system admin.'}, 
                        status=status.HTTP_401_UNAUTHORIZED)
    elif request.user.is_superuser:
        serializer = TaskSerializerFullAcess(task_post, data=request.data)
    else:
        # this line is essential, since if a normal user updates a entry, it needs to be valitaded again, TaskSerializerFullAcess needed
        task_post.states = 'TV'
        serializer = TaskSerializerFullAcess(task_post, data=request.data)
        
    if serializer.is_valid():
        serializer.save()
        return Response({'success' : "The task with id: '" + str(pk)  + \
                        "' was successfully updated."})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(method='put' , request_body=TaskSerializerFullAcess)
@api_view(['PUT'])
@permission_classes((IsAdminUser,))
def validate_task(request, pk):
    try:
        task_post = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'missing' : 'There is no task with this id.'},
                        status=status.HTTP_404_NOT_FOUND)
    serializer = TaskSerializerFullAcess(task_post, data=request.data)

    if serializer.is_valid():
        serializer.save()
        return Response({'success' : "The task with id: '" + str(pk)  + \
                        "' was successfully updated."})
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_task(request, pk):
    try:
        task_post = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response({'missing' : 'There is no task with this id.'},
                         status=status.HTTP_404_NOT_FOUND)
    operation = task_post.delete()  
    data = {}
    if operation:
        data["success"] = "The task with id: '" + str(pk) + \
                        "' was successfully deleted."
    else:
        data["failure"] = "delete failed"
    return Response(data=data)


# https://www.django-rest-framework.org/api-guide/filtering/
class ListTasks(ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializerBasicAccess
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    #?search=staff&ordering=-loc_geo
    search_fields = ('author__username', 'category', 'loc_geo')
    ordering_filds = ('author__username', 'category', 'loc_geo')  


class ListInvalidTasks(ListAPIView):
    queryset = Task.objects.filter(states__exact="TV")
    serializer_class = TaskSerializerBasicAccess
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('author__username', 'category', 'loc_geo')
    ordering_filds = ('author__username', 'category', 'loc_geo')  

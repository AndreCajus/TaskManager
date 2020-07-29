from django.contrib.auth.models import User
from django.shortcuts import render
from rest_framework import status
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view, permission_classes
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.generics import ListAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from drf_yasg.utils import swagger_auto_schema

from account.serializers import AccountSerializer

@swagger_auto_schema(method='post' , request_body=AccountSerializer)
@api_view(['POST', ])
@permission_classes(()) # doenst make sense to have permissions here
def create_account(request):
    serializer = AccountSerializer(data=request.data)
    data = {}
    if serializer.is_valid():
        account = serializer.save()
        data['response'] = "The account of the user '" + account.username + \
                            "' was successfuly registred!"
        token = Token.objects.get(user=account).key
        data['token'] = token
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes((IsAuthenticated,))
def get_account(request, username):
    try:
        account_post = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account_post)
    return Response(serializer.data)


@swagger_auto_schema(method='put' , request_body=AccountSerializer)
@api_view(['PUT'])
@permission_classes((IsAuthenticated,))
def put_account(request, username):
    try:
        account_post = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    serializer = AccountSerializer(account_post, data=request.data)

    if account_post.username != request.user and not request.user.is_superuser:
        return Response({'response': "Only an admin or the account user can edit the account!"}) 
                        #status=status.HTTP_401_UNAUTHORIZED)
        
    r_data = {}
    if serializer.is_valid():
        serializer.save()
        r_data["success"] = "The account of the user '" + account_post.username + \
                          "' was updated successfully!"
        return Response(data=r_data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE'])
@permission_classes((IsAuthenticated,))
def delete_account(request, username):
    try:
        account_post = User.objects.get(username=username)
    except User.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND) 
    if account_post.username != request.user and not request.user.is_superuser:
        return Response({'response': "Only an admin or the account user can edit the account!"})
                        #status=status.HTTP_401_UNAUTHORIZED)

    operation = account_post.delete()  
    r_data = {}
    if operation:
        r_data["success"] = "The account of the user '" + account_post.username + \
                          "' was deleted successfully!"
    else:
        r_data["failure"] = "The account delete for the user '" + account_post.username + \
                          "' failed!"
    return Response(r_data)


# https://www.django-rest-framework.org/api-guide/filtering/
class ListAccounts(ListAPIView):
    queryset = User.objects.all()
    serializer_class = AccountSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)
    pagination_class = PageNumberPagination
    filter_backends = (SearchFilter, OrderingFilter)
    search_fields = ('email', 'username')
    ordering_filds = ('email', 'username')

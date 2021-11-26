from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import BookSerializer, RegisterSerializer
from .models import BookModel, User
from django.contrib.auth import login, authenticate
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.generics import CreateAPIView
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
'''
@api_view(['GET','POST'])
def BookView(request):
    if request.method == 'GET':
        book_queryset = BookModel.objects.all()
        serializer = BookSerializer(book_queryset, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = BookSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
'''

class BookView(APIView):
    queryset = BookModel
    serializer_class = BookSerializer
    def get(self, request, format=None):
        snippets = self.queryset.objects.all()
        serializer = self.serializer_class(snippets, many=True)
        return Response(serializer.data)
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RegisterView(APIView):
    serializer_class = RegisterSerializer
    '''
    context={}
    ['username','password']
    context['confirm_password']=serializer_class.confirm_password
    '''
    def post(self,request, format=None):
        serializer = self.serializer_class(data=request.data)
        #context['confirm_password']=confirm_password
        if serializer.is_valid() :
            serializer.validated_data['password'] = make_password(serializer.validated_data.get('password'))
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    serializer_class = RegisterSerializer
    #username = '' #request.POST.get('username')
    #raw_password = '' #request.POST.get('password')
    def post(self, request, format=None):
        username = request.POST.get('username')
        raw_password = request.POST.get('password')
        user = authenticate(username=username, password=raw_password)
        if user:
            login(request, user)
            return redirect('book-api')
        else:
            return redirect('register-api')

'''
class RegisterView(CreateAPIView):

    model = User
    permission_classes = [
        permissions.AllowAny # Or anon users can't register
    ]
    serializer_class = RegisterSerializer
'''

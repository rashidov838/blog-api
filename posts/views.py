# from rest_framework import generics, permissions # new
# from rest_framework import generics
from rest_framework import viewsets # new
from django.contrib.auth import get_user_model
from .models import Post
from .serializers import PostSerializer,UserSerializer
from .permissions import IsAuthorOrReadOnly
from rest_framework.permissions import IsAdminUser
# class PostList(generics.ListCreateAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer
# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = (IsAuthorOrReadOnly,) # new
#     queryset = Post.objects.all()
#     serializer_class = PostSerializer


# class UserList(generics.ListCreateAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer
# class UserDetail(generics.RetrieveUpdateDestroyAPIView): # new
#     queryset = get_user_model().objects.all()
#     serializer_class = UserSerializer



class PostViewSet(viewsets.ModelViewSet): # new
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer   
class UserViewSet(viewsets.ModelViewSet): # new
    permission_classes=[IsAdminUser]
    queryset = get_user_model().objects.all()
    serializer_class = UserSerializer   
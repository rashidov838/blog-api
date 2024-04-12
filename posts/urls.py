from django.urls import path 

# from .views import PostList,PostDetail,UserDetail,UserList
from rest_framework.routers import SimpleRouter
from .views import UserViewSet,PostViewSet
# urlpatterns = [
#     path("<int:pk>/", PostDetail.as_view(), name="post_detail"),
#     path("", PostList.as_view(), name="post_list"),
#     path("users/", UserList.as_view()), # new
#     path("users/<int:pk>/", UserDetail.as_view()), # new
# ]

router = SimpleRouter()
router.register("users", UserViewSet, basename="users")
router.register("", PostViewSet, basename="posts")
urlpatterns = router.urls 
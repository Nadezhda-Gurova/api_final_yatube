from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_ver1 = DefaultRouter()

router_ver1.register(r'posts', PostViewSet, basename='posts')
router_ver1.register(r'groups', GroupViewSet, basename='groups')
router_ver1.register(
    r'posts/(?P<post_id>\d+)/comments', CommentViewSet, basename='comments'
)
router_ver1.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_ver1.urls)),
]

from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>[\w.@+-]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path(
        'v1/follow/',
        FollowViewSet.as_view({'get': 'list', 'post': 'create'}),
        name='follow'
    ),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
    path('v1/', include(router.urls)),
]

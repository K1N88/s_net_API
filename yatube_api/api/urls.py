from django.urls import path, include
from rest_framework.routers import SimpleRouter
from rest_framework.authtoken import views

from .views import PostViewSet, GroupViewSet, CommentViewSet

router = SimpleRouter()
router.register('posts', PostViewSet, basename='post')
router.register('groups', GroupViewSet, basename='group')
router.register(
    r'posts/(?P<post_id>[\w.@+-]+)/comments',
    CommentViewSet,
    basename='comment'
)

urlpatterns = [
    path('api/v1/api-token-auth/', views.obtain_auth_token),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('api/v1/', include(router.urls)),
]

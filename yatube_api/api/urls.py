from django.urls import include, path
from rest_framework.routers import SimpleRouter
from api.views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet


router = SimpleRouter()

router.register('posts', PostViewSet, basename='posts')
router.register(
    'posts/(?P<post_id>\\d+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt'))
]

from django.urls import include,path

from rest_framework.routers import DefaultRouter

from .views import EventViewSet,CommentListCreateAPIView,ComementDestroyAPIView,EventFavoriteAPIView

router = DefaultRouter(trailing_slash=False)

router.register(r'events',EventViewSet)

app_name = 'events'

urlpatterns = [
    path('',include(router.urls)),

    path('events/<slug:event_slug>/comments',CommentListCreateAPIView.as_view()),

    path('events/<slug:event_slug>/comments/<int:comment_id>',ComementDestroyAPIView.as_view()),

    path('events/<slug:event_slug>/favorite', EventFavoriteAPIView.as_view()),

]

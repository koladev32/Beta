from django.urls import include,path

from rest_framework.routers import DefaultRouter

from .views import EventViewSet

router = DefaultRouter(trailing_slash=False)

router.register(r'events',EventViewSet)

app_name = 'events'

urlpatterns = [
    path('',include(router._urls)),
]

from django.urls import path

from .views import ProfileRetrieveAPIView,ProfileFollowAPI

app_name='profiles'

urlpatterns = [
    path('profiles/<str:email>', ProfileRetrieveAPIView.as_view()),
    path('profiles/<str:email>/follow', ProfileFollowAPI.as_view()),
]

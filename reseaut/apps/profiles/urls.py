from django.urls import path

from .views import ProfileRetrieveAPIView

app_name='profiles'

urlpatterns = [
    path('profiles/<str:email>', ProfileRetrieveAPIView.as_view()),
]

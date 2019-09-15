from django.urls import include, path

from . import views

urlpatterns = [
    path('users/', views.UserListView.as_view()),
    path('leaverequests/', views.ApplicationListView.as_view()),
    path('leaverequests/create/', views.ApplicationCreate.as_view()),
    path('leaverequest/<int:pk>/', views.ApplicationDetail.as_view()),
]

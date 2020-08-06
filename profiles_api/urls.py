from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('Hello-View',views.HelloViewSet,basename='HellView')
router.register('profile',views.UserProfileViewSet)
urlpatterns = [
    path('Hello-api',views.HelloApiView.as_view()),
    path('login',views.UserLoginApiView.as_view()),
    path('',include(router.urls))
]

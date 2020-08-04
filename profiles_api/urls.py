from django.urls import path,include
from profiles_api import views
from rest_framework.routers import DefaultRouter
router=DefaultRouter()
router.register('Hello-View',views.HelloViewSet,basename='HellView')
urlpatterns = [
    path('Hello-api',views.HelloApiView.as_view()),
    path('',include(router.urls))
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('post', views.PostViewSet) # 2개 URL을 만들어 줍니다.

# router.urls 에 리스트 형태로 존재한다.

urlpatterns = [
    path('mypost/<int:pk>/', views.PostDetailAPIView.as_view()),
    # path('public/', views..as_view()),
    path('', include(router.urls))
]


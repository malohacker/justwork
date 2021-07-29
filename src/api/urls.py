from django.urls import include, path
from rest_framework import routers

from api import views

# router = routers.DefaultRouter()
# router.register(r'pages', views.PageListView.as_view(), basename='page')

urlpatterns = [
    # path('', include(router.urls)),
    path('pages/', views.PageListView.as_view(), name='page-list'),
    path('pages/<int:pk>/', views.PageDetailView.as_view(), name='page-detail'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
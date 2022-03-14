from django.contrib import admin
from django.urls import path, re_path
from test_task import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hi),
    path('', views.pusto),
    # path(r'name=<str:name>&message=<str:message>/', views.hi)
]
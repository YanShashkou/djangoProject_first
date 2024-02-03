from django.contrib import admin
from django.urls import path,include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.horoscopes, name='horoscopes'),
    path('<znak>', views.get_info, name='znak')

]
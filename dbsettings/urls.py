from django.urls import path

from dbsettings.views import site_settings, app_settings


urlpatterns = [
    path('', site_settings, name='site_settings'),
    path('<app_label>/', app_settings, name='app_settings'),
]

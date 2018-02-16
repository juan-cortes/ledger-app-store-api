from django.urls import path
from api import views
from rest_framework_swagger.views import get_swagger_view

schema_view = get_swagger_view(title='Manager API')

urlpatterns = [
    path('doc', schema_view),
    path('users', views.UserList.as_view()),
    path('user/<int:pk>', views.UserDetail.as_view()),
    path('auth', views.login),
    path('finish_auth', views.finish_login),
    path('key_registration', views.RegisterKey.as_view()),
    path('protected', views.protected),
]
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView

from api.views import CreateUser, RegisterUser

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/v1/auth/signup/', CreateUser.as_view()),
    path('api/v1/auth/token/', RegisterUser.as_view()),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]

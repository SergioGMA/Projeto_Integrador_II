from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from vacina.api import VacinaViewSet, BannerViewSet, ProfileViewSet, LoginView


router = routers.DefaultRouter()
router.register(r'vacinas', VacinaViewSet, basename='Vacinas')
router.register(r'profile', ProfileViewSet, basename='Profile')
router.register(r'banner', BannerViewSet, basename='Banner')

urlpatterns = [
    #path('', TemplateView.as_view(template_name="index.html")),
    #path('cadastro/', CadastroView.as_view(template_name="cadastro.html")),
    #path('vacina/', VacinaView.as_view(template_name="vacina.html")),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('rest-auth/', include('rest_auth.urls')),
    path('login/', LoginView.as_view(), name = 'login')
]

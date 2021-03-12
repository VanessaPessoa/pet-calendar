from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app.views import UserViewSet, PetViewSet, VacinaViewSet

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'pets', PetViewSet)
router.register(r'vacinas', VacinaViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls'))
]


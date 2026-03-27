from django.contrib import admin
from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from users.views import RegisterView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers

# 🔹 Serializer personalizado para usar email como campo de login
class EmailTokenObtainPairSerializer(TokenObtainPairSerializer):
    username_field = 'email'

    def validate(self, attrs):
        # Reemplazamos username por email para validación
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            raise serializers.ValidationError("Debe ingresar email y contraseña.")

        # Asignamos el email como "username" interno
        attrs['username'] = email
        return super().validate(attrs)


# 🔹 View personalizada que usa nuestro serializer
class EmailTokenObtainPairView(TokenObtainPairView):
    serializer_class = EmailTokenObtainPairSerializer


# 🔹 Rutas principales
urlpatterns = [
    path('admin/', admin.site.urls),

    # Endpoints de autenticación
    path('api/token/', EmailTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # Registro de usuario
    path('api/register/', RegisterView.as_view(), name='register'),
]

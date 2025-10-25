from rest_framework import generics, permissions
from .models import User
from .serializers import RegisterSerializer
from rest_framework.response import Response
from rest_framework import status

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [permissions.AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response(
            {"message": "Usuario registrado correctamente"},
            status=status.HTTP_201_CREATED
        )

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from users.models import User

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        # Reemplazar 'username' por 'email'
        email = attrs.get("email")
        password = attrs.get("password")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise serializers.ValidationError({"detail": "Usuario no encontrado."})

        if not user.check_password(password):
            raise serializers.ValidationError({"detail": "Contraseña incorrecta."})

        if not user.is_active:
            raise serializers.ValidationError({"detail": "Usuario inactivo."})

        # Usa la validación base
        data = super().validate({
            "username": user.email,  # Django aún usa "username" internamente
            "password": password
        })

        return data


class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

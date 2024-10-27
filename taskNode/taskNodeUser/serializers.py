from djoser.serializers import UserCreateSerializer
from .models import CustomUser


class CustomUserSerializer(UserCreateSerializer):
    class Meta(UserCreateSerializer.Meta):
        model = CustomUser
        fields = ('id', 'email', 'username', 'first_name', 'last_name', 'password', 'role')


    def create(self, validated_data):
        return super().perform_create(validated_data) 
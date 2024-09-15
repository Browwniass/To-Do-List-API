from common.serializers.mixins import ExtendedModelSerializer
from users.models import User


class UserShortSerializer(ExtendedModelSerializer):
    class Meta:
        model = User
        fields = (
            'id',
            'username',
        )
        read_only_fields = (
            'id',
            'username',
        )
from common.serializers.mixins import ExtendedModelSerializer
from tasks.models.task import Task


class TaskListSerializer(ExtendedModelSerializer):
    class Meta:
        model = Task
        fields = (
            'id',
            'name',
            'status',
            'created',
            'owner',
        )
        read_only_fields = (
            'owner',
            'created',
        )


class TaskDetailSerializer(ExtendedModelSerializer):
    class Meta:
        model = Task
        fields = ('__all__')
        read_only_fields = (
            'owner',
            'created',
        )

    def create(self, validated_data):
        request = self.context.get('request')
        validated_data['owner'] = request.user
        return super().create(validated_data)

from rest_framework import serializers
from api.models import QNaModel, QnaOptionModel
from api.serializers import ServiceSerializer

class getQNASerializer(serializers.ModelSerializer):
    service = ServiceSerializer()
    options = serializers.SerializerMethodField()
    class Meta:
        model = QNaModel
        fields = (
           'id', 'service', 'name', 'options'
        )

    def get_options(self, obj):
        qna_obj = QnaOptionModel.objects.filter(qna=obj.id)
        serializer = getQnaOptionSerializer(qna_obj, many=True)
        return serializer.data

class getQnaOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = QnaOptionModel
        fields = (
           'id', 'option'
        )
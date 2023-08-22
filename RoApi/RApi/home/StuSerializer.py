from rest_framework import serializers
from .models import Stu
class StuSerializer(serializers.ModelSerializer):
    class Meta:
        model=Stu
        fields='__all__'
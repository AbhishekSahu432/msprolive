from rest_framework import viewsets
from .StuSerializer import StuSerializer
from .models import Stu
class StuViewset(viewsets.ModelViewSet):
    queryset=Stu.objects.all()
    serializer_class=StuSerializer
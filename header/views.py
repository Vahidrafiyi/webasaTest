from rest_framework import viewsets

from .serializers import *
from .models import *
from blog.permissions import IsAdminUserOrReadOnly


class MenuViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Menu.objects.filter(parent__isnull=True)
    serializer_class = MenuSerializer

class LogoViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAdminUserOrReadOnly,)
    queryset = Logo.objects.all()
    serializer_class = LogoSerializer


    # def get_permissions(self):
    #     # Your logic should be all here
    #     if self.request.method == 'GET':
    #         self.permission_classes = [IsAuthenticated, ]
    #     else:
    #         self.permission_classes = [IsAdminUser, ]
    #
    #     return super(MenuList, self).get_permissions()



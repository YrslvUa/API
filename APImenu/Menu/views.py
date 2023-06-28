from rest_framework import generics
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Menu
from .permissions import IsAdminOrReadOnly
from .serializers import MenuSerializer


class MenuAPIListPagination(PageNumberPagination):
    page_size = 3
    page_size_query_param = 'page_size'
    max_page_size = 5


class MenuAPIList(generics.ListCreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)
    pagination_class = MenuAPIListPagination


class MenuAPICreate(generics.CreateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

class MenuAPIUpdate(generics.RetrieveUpdateAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAuthenticated,)


class MenuAPIDestroy(generics.RetrieveDestroyAPIView):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = (IsAdminOrReadOnly,)

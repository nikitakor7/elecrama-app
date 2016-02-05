import django_filters
from bedroom.models import bedroom
from bedroom.serializers import bedroomSerializer
from rest_framework import filters
from rest_framework import generics


class bedroomList(generics.ListCreateAPIView):
    queryset = bedroom.objects.all()
    serializer_class = bedroomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('switch')


class bedroomDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = bedroom.objects.all()
    serializer_class = bedroomSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('switch')

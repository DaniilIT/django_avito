from rest_framework.viewsets import ModelViewSet

from ads.models import Location
from ads.serializers import LocationSerializer


class LocationViewSet(ModelViewSet):
    queryset = Location.objects.all()
    serializer_class = LocationSerializer

# class LocationViewSet(viewsets.ViewSet):
#     def list(self, request):
#         queryset = Location.objects.all()
#         serializer = LocationSerializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Location.objects.all()
#         location = get_object_or_404(queryset, pk=pk)
#         serializer =  (location)
#         return Response(serializer.data)
#
#     def create(self, request):
#         serializer = LocationSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(serializer)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def update(self, request, pk=None):
#         queryset = Location.objects.all()
#
#         location = get_object_or_404(queryset, pk=pk)
#
#         serializer = LocationSerializer(location, data=request.data, partial=partial)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(serializer)
#         return Response(serializer.data)
#
#
#     def partial_update(self, request, pk=None):
#         kwargs['partial'] = True
#         return self.update(request, *args, **kwargs)
#
#
#     def destroy(self, request, pk=None):
#         queryset = Location.objects.all()
#         location = get_object_or_404(queryset, pk=pk)
#         location.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

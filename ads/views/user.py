import json

from django.core.exceptions import ValidationError
from django.core.paginator import Paginator
from django.db.models import Count
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from rest_framework.generics import CreateAPIView, ListAPIView, RetrieveAPIView, UpdateAPIView

from ads.models import User, Location, Ad
from ads.serializers import UserCreateSerializer, UserListSerializer, UserDetailSerializer, UserUpdateSerializer
from avito import settings


def get_object_or_none(model, objects, **kwargs):
    try:
        return objects.get(**kwargs)
    except model.DoesNotExist:
        return None


class UserListView(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserListSerializer

    # def get(self, request, *args, **kwargs):
    #     super().get(request, *args, **kwargs)
    #
    #     # self.object_list = self.object_list.select_related('author').select_related('category')
    #     #
    #     # self.object_list = self.object_list.order_by('-price')
    #     total_ads = self.object_list.filter(ad__is_published=True).annotate(total_ads=Count('ad'))
    #     self.object_list = self.object_list.prefetch_related('location').order_by('username')
    #
    #     paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
    #     page_number = request.GET.get('page')
    #     page_obj = paginator.get_page(page_number)
    #
    #     users = [{
    #         'id': user.id,
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "username": user.username,
    #         "role": user.role,
    #         "age": user.age,
    #         "location": list(map(str, user.location.all())),
    #         'total_ads': get_object_or_none(User, total_ads, pk=user.id).total_ads
    #         if get_object_or_none(User, total_ads, pk=user.id) else 0,  # user.total_ads
    #     } for user in page_obj]
    #
    #     return JsonResponse(data={
    #         'items': users,
    #         'per_page': settings.TOTAL_ON_PAGE,
    #         'num_pages': paginator.num_pages,
    #         'total': paginator.count  # количество записей
    #     }, json_dumps_params={"ensure_ascii": False})

class UserDetailView(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer

    # def get(self, request, *args, **kwargs):
    #     user = self.get_object()
    #
    #     # self.object_list = self.object_list.filter(ad__is_published=True).annotate(total_ads=Count('ad'))
    #
    #     return JsonResponse({
    #         'id': user.id,
    #         "first_name": user.first_name,
    #         "last_name": user.last_name,
    #         "username": user.username,
    #         "password": user.password,
    #         "role": user.role,
    #         "age": user.age,
    #         "location": list(map(str, user.location.all())),
    #         'total_ads': Ad.objects.filter(author_id=user.id, is_published=True).count(),
    #     }, json_dumps_params={"ensure_ascii": False})


# @method_decorator(csrf_exempt, name='dispatch')
# class UserCreateView(CreateView):
#     model = User
#     fields = ('first_name', 'last_name', 'username', 'password', 'role', 'age', 'location')
#
#     def post(self, request, *args, **kwargs):
#         user_data = json.loads(request.body)
#
#         new_user = User.objects.create(
#             first_name=user_data.get('first_name'),
#             last_name=user_data.get('last_name'),
#             username=user_data.get('username'),
#             password=user_data.get('password'),
#             role=user_data.get('role'),
#             age=user_data.get('age')
#         )
#
#         for loc in user_data['location']:
#             loc_obj, created = Location.objects.get_or_create(name=loc)
#             print(loc_obj, created)
#             new_user.location.add(loc_obj)
#
#         new_user.save()
#
#         return JsonResponse({
#             'id': new_user.id,
#             "first_name": new_user.first_name,
#             "last_name": new_user.last_name,
#             "username": new_user.username,
#             "password": new_user.password,
#             "role": new_user.role,
#             "age": new_user.age,
#             "location": list(map(str, new_user.location.all())),
#         }, json_dumps_params={"ensure_ascii": False}, status=302)
class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer


# @method_decorator(csrf_exempt, name='dispatch')
# class UserUpdateView(UpdateView):
#     model = User
#     fields = ('first_name', 'last_name', 'username', 'password', 'role', 'age', 'location')
#
#     def patch(self, request, *args, **kwargs):
#         super().post(request, *args, **kwargs)
#
#         user_data = json.loads(request.body)
#         self.object.first_name = user_data['first_name']
#         self.object.last_name = user_data['last_name']
#         self.object.username = user_data['username']
#         self.object.password = user_data['password']
#         self.object.role = user_data['role']
#         self.object.age = user_data['age']
#
#         for loc in self.object.location.all():
#             self.object.location.remove(loc)
#
#         for loc in user_data['location']:
#             loc_obj, created = Location.objects.get_or_create(name=loc)
#             self.object.location.add(loc_obj)
#
#         try:
#             self.object.full_clean()
#         except ValidationError as error:
#             return JsonResponse(error.message_dict, status=422)  # Unprocessable Entity
#
#         self.object.save()
#
#         return JsonResponse({
#             'id': self.object.id,
#             "first_name": self.object.first_name,
#             "last_name": self.object.last_name,
#             "username": self.object.username,
#             "password": self.object.password,
#             "role": self.object.role,
#             "age": self.object.age,
#             "location": list(map(str, self.object.location.all())),
#             'total_ads': Ad.objects.filter(author_id=self.object.id, is_published=True).count(),
#         }, json_dumps_params={"ensure_ascii": False}, status=302)

class UserUpdateView(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserUpdateSerializer

@method_decorator(csrf_exempt, name='dispatch')
class UserDeleteView(DeleteView):
    model = User
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({}, status=204)
        # return redirect(self.get_success_url())

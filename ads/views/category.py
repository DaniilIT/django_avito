import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from ads.models import Category


class CatListView(ListView):
    model = Category

    # queryset = Category.object.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        self.object_list = self.object_list.order_by('name')

        return JsonResponse(data=[{
            'id': category.id,
            'name': category.name,
        } for category in self.object_list],
            safe=False, json_dumps_params={"ensure_ascii": False})


class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        category = self.get_object()

        return JsonResponse({
            'id': category.id,
            'name': category.name
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CatCreateView(CreateView):
    model = Category
    fields = ('name',)

    def post(self, request, *args, **kwargs):
        category_data = json.loads(request.body)

        new_category = Category.objects.create(
            name=category_data.get('name')
        )

        return JsonResponse({
            'id': new_category.id,
            'name': new_category.name
        }, json_dumps_params={"ensure_ascii": False}, status=302)


@method_decorator(csrf_exempt, name='dispatch')
class CatUpdateView(UpdateView):
    model = Category
    fields = ('name',)

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data['name']
        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            'name': self.object.name
        }, json_dumps_params={"ensure_ascii": False}, status=302)


@method_decorator(csrf_exempt, name='dispatch')
class CatDeleteView(DeleteView):
    model = Category
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({}, status=204)
        # return redirect(self.get_success_url())

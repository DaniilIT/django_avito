import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from ads.models import Ad


class AdListView(ListView):
    model = Ad

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        if is_published := request.GET.get("is_published"):
            is_published = True if is_published == 'true' else False
            self.object_list = self.object_list.filter(is_published=is_published)

        self.object_list = self.object_list.select_related('author').select_related('category')

        return JsonResponse(data=[{
            'id': ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            'image': ad.image.url if ad.image else None,
            "author": ad.author.username,
            "category": ad.category.name if ad.category else None,
        } for ad in self.object_list],
            safe=False, json_dumps_params={"ensure_ascii": False})


class AdDetailView(DetailView):
    model = Ad

    def get(self, request, *args, **kwargs):
        ad = self.get_object()

        return JsonResponse({
            'id': ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "author": ad.author.username,
            "category": ad.category.name if ad.category else None,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ('name', 'price', 'description', 'is_published', 'image', 'author_id', 'category_id')

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        ad = Ad.object.create(name=ad_data.get('name'),
                              price=ad_data.get('price'),
                              description=ad_data.get('description'),
                              is_published=ad_data.get('is_published'),
                              image=ad_data.get('image'),
                              author_id=ad_data.get('author_id'),
                              category_id=ad_data.get('category_id'))

        return JsonResponse({
            'id': ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "author": ad.author.username,
            "category": ad.category.name if ad.category else None,
        }, json_dumps_params={"ensure_ascii": False}, status=302)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ('name', 'price', 'description', 'is_published', 'image', 'author_id', 'category_id')

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        category_data = json.loads(request.body)
        self.object.name = category_data['name']
        self.object.price = category_data['price']
        self.object.description = category_data['description']
        self.object.is_published = category_data['is_published']
        self.object.image = category_data['image']
        self.object.author_id = category_data['author_id']
        self.object.category_id = category_data['category_id']

        self.object.save()

        return JsonResponse({
            'id': self.object.id,
            "name": self.object.name,
            "price": self.object.price,
            "description": self.object.description,
            "is_published": self.object.is_published,
            "image": self.object.image.url if self.object.image else None,
            "author": self.object.author.username,
            "category": self.object.category.name if self.object.category else None,
        }, json_dumps_params={"ensure_ascii": False}, status=302)


@method_decorator(csrf_exempt, name='dispatch')
class AdDeleteView(DeleteView):
    model = Ad
    success_url = '/'

    def delete(self, request, *args, **kwargs):
        super().delete(request, *args, **kwargs)
        return JsonResponse({}, status=204)
        # return redirect(self.get_success_url())

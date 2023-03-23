import json

from django.core.paginator import Paginator
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView

from ads.models import Ad, User, Category
from avito import settings


class AdListView(ListView):
    model = Ad

    # queryset = Ad.object.all()

    def get(self, request, *args, **kwargs):
        super().get(request, *args, **kwargs)

        if is_published := request.GET.get("is_published"):
            is_published = True if is_published == 'true' else False
            self.object_list = self.object_list.filter(is_published=is_published)

        self.object_list = self.object_list.select_related('author').select_related('category')

        self.object_list = self.object_list.order_by('-price')

        paginator = Paginator(self.object_list, settings.TOTAL_ON_PAGE)
        page_number = request.GET.get('page')  # , 0
        page_obj = paginator.get_page(page_number)

        ads = [{
            'id': ad.id,
            "name": ad.name,
            "price": ad.price,
            "description": ad.description,
            "is_published": ad.is_published,
            "image": ad.image.url if ad.image else None,
            "author_id": ad.author_id,
            "author": ad.author.username,
            "category_id": ad.category_id,
            "category": ad.category.name if ad.category else None,
        } for ad in page_obj]

        return JsonResponse(data={
            'items': ads,
            'per_page': settings.TOTAL_ON_PAGE,
            'num_pages': paginator.num_pages,
            'total': paginator.count  # количество записей
        }, json_dumps_params={"ensure_ascii": False})


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
            "author_id": ad.author_id,
            "author": ad.author.username,
            "category_id": ad.category_id,
            "category": ad.category.name if ad.category else None,
        }, json_dumps_params={"ensure_ascii": False})


def get_object_or_none(model, **kwargs):
    try:
        return model.objects.get(**kwargs)
    except model.DoesNotExist:
        return None


@method_decorator(csrf_exempt, name='dispatch')
class AdCreateView(CreateView):
    model = Ad
    fields = ('name', 'price', 'description', 'is_published', 'author', 'category')

    def post(self, request, *args, **kwargs):
        ad_data = json.loads(request.body)

        author = get_object_or_404(User, pk=ad_data['author_id'])
        category = get_object_or_none(Category, pk=ad_data.get('category_id'))

        new_ad = Ad.objects.create(
            name=ad_data.get('name'),
            price=ad_data.get('price'),
            description=ad_data.get('description'),
            is_published=ad_data.get('is_published'),
            author=author,
            category=category
        )

        return JsonResponse({
            'id': new_ad.id,
            "name": new_ad.name,
            "price": new_ad.price,
            "description": new_ad.description,
            "is_published": new_ad.is_published,
            "image": new_ad.image.url if new_ad.image else None,
            "author": new_ad.author.username,
            "category": new_ad.category.name if new_ad.category else None,
        }, json_dumps_params={"ensure_ascii": False}, status=302)


@method_decorator(csrf_exempt, name='dispatch')
class AdUpdateView(UpdateView):
    model = Ad
    fields = ('name', 'price', 'description', 'is_published', 'author', 'category')

    def patch(self, request, *args, **kwargs):
        super().post(request, *args, **kwargs)

        ad_data = json.loads(request.body)
        self.object.name = ad_data['name']
        self.object.price = ad_data['price']
        self.object.description = ad_data['description']
        self.object.is_published = ad_data['is_published']
        self.object.author = get_object_or_404(User, pk=ad_data['author_id'])
        self.object.category = get_object_or_none(Category, pk=ad_data['category_id'])
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

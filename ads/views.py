import json

from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import DetailView

from ads.models import Ads, Category


def root(request):
    return JsonResponse({'status': 'ok'})


@method_decorator(csrf_exempt, name='dispatch')
class CatView(View):
    def get(self, request):
        categories = Category.objects.all()

        response = []
        for category in categories:
            response.append({
                'id': category.id,
                'name': category.name,
            })

        return JsonResponse(response, safe=False,
                            json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        category_data = json.loads(request.body)

        category = Category.object.create(name=category_data.get('name'))

        return JsonResponse({'id': category.id, 'name': category.name},
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class CatDetailView(DetailView):
    model = Category

    def get(self, request, *args, **kwargs):
        try:
            category = self.get_object()
        except self.model.DoesNotExist as exc:
            return JsonResponse({'error': str(exc)}, status=404)

        return JsonResponse({'id': category.id, 'name': category.name},
                            json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdView(View):
    def get(self, request):
        ads = Ads.objects.all()

        if is_published := request.GET.get("is_published"):
            is_published = True if is_published == 1 else False
            ads = ads.filter(is_published=is_published)

        response = []
        for ad in ads:
            response.append({
                'id': ad.id,
                "name": ad.name,
                "author": ad.author,
                "price": ad.price,
                "description": ad.description,
                "address": ad.address,
                "is_published": ad.is_published,
            })

        return JsonResponse(response, safe=False,
                            json_dumps_params={"ensure_ascii": False})

    def post(self, request):
        ad_data = json.loads(request.body)

        ad = Ads.object.create(id=ad_data.get('id'),
                               name=ad_data.get('name'),
                               author=ad_data.get('author'),
                               price=ad_data.get('price'),
                               description=ad_data.get('description'),
                               address=ad_data.get('address'),
                               is_published=ad_data.get('is_published'))

        return JsonResponse({
            'id': ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, json_dumps_params={"ensure_ascii": False})


@method_decorator(csrf_exempt, name='dispatch')
class AdDetailView(DetailView):
    model = Ads

    def get(self, request, *args, **kwargs):
        try:
            ad = self.get_object()
        except self.model.DoesNotExist as exc:
            return JsonResponse({'error': str(exc)}, status=404)

        return JsonResponse({
            'id': ad.id,
            "name": ad.name,
            "author": ad.author,
            "price": ad.price,
            "description": ad.description,
            "address": ad.address,
            "is_published": ad.is_published,
        }, json_dumps_params={"ensure_ascii": False})

from django.shortcuts import render 
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin 
from .models import Product, Order
from django.urls import reverse_lazy
from django.db.models import Q # for search method
from django.http import JsonResponse
import json



class ProductsListView(ListView):
    model = Product
    template_name = 'list.html'


class ProductsDetailView(DetailView):
    model = Product
    template_name = 'detail.html'


class SearchResultsListView(ListView):
	model = Product
	template_name = 'search_results.html'

	def get_queryset(self): # new
		query = self.request.GET.get('q')
		return Product.objects.filter(
		Q(product_name__icontains=query) | Q(seller__icontains=query)
		)

class ProductCheckoutView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = 'checkout.html'
    login_url     = 'login'


def paymentComplete(request):
	body = json.loads(request.body)
	print('BODY:', body)
	product = Product.objects.get(id=body['productId'])
	Order.objects.create(
		product=product
	)
	return JsonResponse('Payment completed!', safe=False)


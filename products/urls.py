
from django.urls import path
from .views import ProductsListView, ProductsDetailView, ProductCheckoutView, paymentComplete, SearchResultsListView


urlpatterns = [
    path('', ProductsListView.as_view(), name = 'list'),
    path('<int:pk>/', ProductsDetailView.as_view(), name = 'detail'),
    path('<int:pk>/checkout/', ProductCheckoutView.as_view(), name = 'checkout'),
    path('complete/', paymentComplete, name = 'complete'),
    path('search/', SearchResultsListView.as_view(), name = 'search_results'),
]
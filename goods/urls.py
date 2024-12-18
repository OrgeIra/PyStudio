from django.urls import path
from .views import product, catalog

app_name = "goods"

urlpatterns = [
    path("<slug:category_slug>/", catalog, name="catalog"),
    path('product/<slug:product_slug>/', product, name="product"),
]

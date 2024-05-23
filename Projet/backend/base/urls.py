from django.urls import path
from .views import Home, ProductList, AddToCart, CartDetail, UpdateCart, RemoveFromCart

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('products/', ProductList.as_view(), name='product_list'),
    path('cart/', CartDetail.as_view(), name='cart_detail'),
    path('cart/add/<int:product_id>/', AddToCart.as_view(), name='add_to_cart'),
    path('cart/update/<int:item_id>/', UpdateCart.as_view(), name='update_cart'),
    path('cart/remove/<int:item_id>/', RemoveFromCart.as_view(), name='remove_from_cart'),
]

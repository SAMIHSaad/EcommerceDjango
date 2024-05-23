from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Product, Cart, CartItem

class Home(View):
    def get(self, request):
        return render(request, "home.html", {})

class ProductList(View):
    def get(self, request):
        products = Product.objects.all()
        return render(request, "listProducts.html", {'produits': products})

class AddToCart(View):
    @method_decorator(login_required)
    def post(self, request, product_id):
        product = get_object_or_404(Product, id=product_id)
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
        
        cart_item.quantity += 1
        cart_item.save()
        
        return redirect('cart_detail')

class CartDetail(View):
    @method_decorator(login_required)
    def get(self, request):
        cart = get_object_or_404(Cart, user=request.user)
        return render(request, 'cart_detail.html', {'cart': cart})

class UpdateCart(View):
    @method_decorator(login_required)
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        quantity = int(request.POST.get('quantity', 1))
        
        if quantity > 0:
            cart_item.quantity = quantity
            cart_item.save()
        else:
            cart_item.delete()
        
        return redirect('cart_detail')

class RemoveFromCart(View):
    @method_decorator(login_required)
    def post(self, request, item_id):
        cart_item = get_object_or_404(CartItem, id=item_id)
        cart_item.delete()
        return redirect('cart_detail')

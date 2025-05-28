from django.shortcuts import render, get_object_or_404, redirect
from .models import Product, CartItem, Cart
from django.contrib import messages
from django.views.decorators.http import require_POST

# Home page with special products and banner
def home_view(request):
    special_products = Product.objects.filter(is_special=True)
    return render(request, 'home.html', {'special_products': special_products})

# Product listing page
def product_list_view(request):
    products = Product.objects.all()
    return render(request, 'product_list.html', {'products': products})

# Product detail page
def product_detail_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product_detail.html', {'product': product})

# Add to cart logic
def add_to_cart_view(request, id):
    product = get_object_or_404(Product, id=id)
    quantity = int(request.POST.get('quantity', 1))
    print("meowwwwwww")
    cart = request.session.get('cart', {})
    if str(id) in cart:
        cart[str(id)] += quantity
    else:
        cart[str(id)] = quantity
    request.session['cart'] = cart

    messages.success(request, f"Added {product.title} to cart.")
    return redirect('cart')

# Cart view
def cart_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal
        })

    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total})


@require_POST
def update_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    action = request.POST.get('action')
    cart = request.session.get('cart', {})

    current_qty = cart.get(str(product_id), 0)
    if action == 'increase' and current_qty < product.stock:
        cart[str(product_id)] = current_qty + 1
    elif action == 'decrease' and current_qty > 1:
        cart[str(product_id)] = current_qty - 1

    request.session['cart'] = cart
    return redirect('cart')

@require_POST
def remove_from_cart(request, product_id):
    cart = request.session.get('cart', {})
    cart.pop(str(product_id), None)
    request.session['cart'] = cart
    return redirect('cart')

# Checkout view
def checkout_view(request):
    cart = request.session.get('cart', {})
    cart_items = []
    total = 0

    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, id=product_id)
        subtotal = product.price * quantity
        total += subtotal
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(request, 'checkout.html', {
        'cart_items': cart_items,
        'total': total
    })


def about_view(request):
    return render(request, 'about.html')

def warranty_view(request):
    return render(request, 'warranty.html')

def contact_view(request):
    return render(request, 'contact.html')



def refund_policy_view(request):
    return render(request, 'refund.html')

def terms_conditions_view(request):
    return render(request, 'terms.html')


def place_order_view(request):
    if request.method == 'POST':
        # Optionally collect customer info here
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        postal_code = request.POST.get('postal_code')

        # For now, you can just clear the cart and show a success message
        request.session['cart'] = {}
        messages.success(request, "Your order has been placed! We'll contact you soon.")

        return redirect('order_success')  # Or redirect to homepage or thank you page

    return redirect('checkout')

def order_success_view(request):
    return render(request, 'order_success.html')

from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import *


urlpatterns = [
    path('', home_view, name='home'),
    path('products/', product_list_view, name='product_list'),
    path('products/<int:id>/', product_detail_view, name='product_detail'),
    path('cart/', cart_view, name='cart'),
    path('cart/update/', update_cart, name='update_cart'),

    path('cart/update/<int:product_id>/', update_cart, name='update_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),

    path('add-to-cart/<int:id>/', add_to_cart_view, name='add_to_cart'),
    path('checkout/', checkout_view, name='checkout'),

    path('about/', about_view, name='about'),
    path('warranty/', warranty_view, name='warranty'),
    path('faq/', faq_page, name='faq_page'),

    path('contact/', contact_view, name='contact'),
    path('refund/', refund_policy_view, name='refund'),
    path('terms/', terms_conditions_view, name='terms'),

     path('checkout/', checkout_view, name='checkout'),

     path('place-order/', place_order_view, name='place_order'),

     path('order-success/', order_success_view, name='order_success'),

]

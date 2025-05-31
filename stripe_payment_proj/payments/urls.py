from django.urls import path
import views

app_name = 'payments'

urlpatterns = [
    path('item/<int:item_id>/', views.item_detail, name='item_detail'),
    path('buy/<int:item_id>/', views.create_checkout_session, name='create_checkout_session'),
    path('success/', views.success, name='success'),
]

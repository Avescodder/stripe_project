import stripe
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Item

stripe.api_key = settings.STRIPE_SECRET_KEY

def item_detail(request, item_id):
    #Product page display with buy button
    item = get_object_or_404(Item, id=item_id)
    context = {
        'item': item,
        'stripe_publishable_key': settings.STRIPE_PUBLISHABLE_KEY,
    }
    return render(request, 'payments/item_detail.html', context)

@csrf_exempt
def create_checkout_session(request, item_id):
    #Creating Stripe checkout session
    if request.method == 'GET':
        item = get_object_or_404(Item, id=item_id)

        try:
            checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[{
                    'price_data': {
                        'currency': 'usd',
                        'product_data': {
                            'name': item.name,
                            'description': item.description,
                        },
                        #here stripe using cents 
                        'unit_amount': int(item.price * 100), 
                    },
                    'quantity': 1,
                }],
                mode='payment',
                success_url=request.build_absolute_uri('/success/'),
                cancel_url=request.build_absolute_uri(f'/item/{item_id}/'),
            )
            return JsonResponse({'id': checkout_session.id})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)

    return JsonResponse({'error': 'Method not allowed'}, status=405)


def success(request):
    #Successful payment page
    return render(request, 'payments/success.html')



import requests
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.http import HttpResponse, JsonResponse

@csrf_exempt
@require_POST
def pay(request):
    amount = request.POST.get('amount')
    order_id = request.POST.get('order_id')

    # create payment request
    data = {
        "method": "cards.create",
        "params": {
            "amount": amount,
            "account[order_id]": order_id,
            "currency": "UZS",
            "callback_url": f"{settings.BASE_URL}/callback"
        },
        "id": 1
    }

    headers = {
        "Content-Type": "application/json",
        "X-Auth": settings.PAYME_MERCHANT_KEY
    }

    response = requests.post(settings.PAYME_API_URL, json=data, headers=headers)

    if response.status_code == 200:
        response_data = response.json()
        return JsonResponse(response_data)
    else:
        return HttpResponse("Payment request failed")

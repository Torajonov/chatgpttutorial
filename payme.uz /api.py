@csrf_exempt
@require_POST
def callback(request):
    data = request.POST.get('data')
    signature = request.POST.get('signature')

    # verify the signature
    if verify_signature(data, signature):
        # handle the payment completion
        return HttpResponse("Payment completed successfully")
    else:
        return HttpResponse("Signature verification failed")

import hashlib

def verify_signature(data, signature):
    m = hashlib.sha256()
    m.update(data.encode('utf-8'))
    m.update(settings.PAYME_MERCHANT_KEY.encode('utf-8'))
    calculated_signature = m.hexdigest()

    return signature == calculated_signature

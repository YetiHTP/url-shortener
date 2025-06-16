import string
import random

def generate_short_url(length=6):
    return ''.join(random.choices(string.ascii_letters + string.digits, k = length))

#base62 from id
BASE62 = string.ascii_letters + string.digits

def encode_base62(num):
    if num == 0:
        return BASE62[0]
    
    base = []
    
    while num > 0:
        num, rem = divmod(num, base)
        base.append(BASE62[rem])
    
    return ''.join(reversed(base))
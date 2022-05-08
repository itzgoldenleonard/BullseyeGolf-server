import random

def generate_key():
    key = random.getrandbits(128)
    key_enc = hex(key)

    with open('/bullseyegolf/credentials/admin_key', 'w') as file:
        file.write(key_enc)

    return key_enc

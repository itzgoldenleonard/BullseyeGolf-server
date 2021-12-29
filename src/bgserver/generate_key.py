import random

key = random.getrandbits(128)
key_enc = hex(key)

print(f'API key:\n{key_enc}')

with open('/bullseyegolf/credentials/admin_key', 'w') as file:
    file.write(key_enc)

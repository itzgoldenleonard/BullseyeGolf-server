import random
from .dataclass import write

def generate_key():
    key = random.getrandbits(128)
    key_enc = hex(key)
    
    write(key_enc, "bullseyegolf/credentials/admin_key")

    return key_enc

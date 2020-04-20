# Import virgil crypto library into python file
from virgil_crypto import VirgilCrypto

# First, create Virgil Crypto object
crypto = VirgilCrypto()

# Create public/private keys for the sender. Default algorithm is EC_X25519
sender_keys = crypto.generate_key_pair()
sender_public_key = sender_keys.public_key
sender_private_key = sender_keys.private_key

# Create data that we want to verify between the two clients. This data won't be sent yet, just for signature validation purposes.
message = "Hey Deren! My location is lat=42.361145,long=-71.057083"
message_data = message.encode()

# Sign the message data with the senders private key.
signature = crypto.generate_signature(message_data, sender_private_key)

# Verify if the message can be decoded with the given public key : "sender_public_key"
verification = crypto.verify_signature(message_data, signature, sender_public_key)

print(verification)
# Import virgil crypto library into python file
from virgil_crypto import VirgilCrypto

# First, create Virgil Crypto object
crypto = VirgilCrypto()

# Create public/private keys for the sender. Default algorithm is EC_X25519
sender_keys = crypto.generate_key_pair()
sender_public_key = sender_keys.public_key
sender_private_key = sender_keys.private_key

# Create public/private keys for the receiver.
receiver_keys = crypto.generate_key_pair()
receiver_public_key = receiver_keys.public_key
receiver_private_key = receiver_keys.private_key

# Create data that we want to verify between the two clients. This data won't be sent yet, just for signature validation purposes.
location = "lat=42.361145,long=-71.057083"
location_data = location.encode()

# List of public keys that will receive the location data
receiver_list = [receiver_public_key]

# Encrypt the data using AES-256
encrypted_data = crypto.encrypt(location_data, *receiver_list)

# Now, this is the receivers side (The person receiving the location from the sender). This would be a separate individual client.
# If we were to use sockets, this would be another file for a different host interacting with the server. The receivers private
# key is available because they are receiving the encrypted message on their device.
decrypted_data = crypto.decrypt(encrypted_data, receiver_private_key)
decrypted_message = bytes(decrypted_data).decode()

print(decrypted_message)
from virgil_crypto import VirgilCrypto

crypto = VirgilCrypto()

# Generate private/public key with EC_X25519
sender_keys = crypto.generate_key_pair()
sender_private_key = sender_keys.private_key
sender_public_key = sender_keys.public_key

# Generate keys for the receiving end of the location.
receiver_keys = crypto.generate_key_pair()
receiver_public_key = receiver_keys.public_key
receiver_private_key = receiver_keys.private_key

# Generate keys for the middle man!
middleman_keys = crypto.generate_key_pair()
middleman_public_key = middleman_keys.public_key
middleman_private_key = middleman_keys.private_key

# Create location to send to receiver. This will be intercepted by the middleman.
location = "lat=42.361145,long=-71.057083"
location_data = location.encode()

# Ok encrypt a message for the receiver. It requires the receivers public key and the message being sent.
receiver_list = [receiver_public_key]
encrypted_data = crypto.encrypt(location_data, *receiver_list)

# Time for the middleman to decrypt data. He is not on the receiver list, so it shouldn't work!
middleman_decrypted_data = crypto.decrypt(encrypted_data, middleman_private_key)

# Decrypt the message from the host. This is the receivers part now. This is why the private key is here
decrypted_data = crypto.decrypt(encrypted_data, receiver_private_key)
decrypted_message = bytes(decrypted_data).decode()

# Print decrypted message for the intended receiver.
print(decrypted_message)

# Print the decrypted data for the middleman.
print(middleman_decrypted_data)
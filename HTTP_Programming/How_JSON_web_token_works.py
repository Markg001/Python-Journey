#  How Does a JSON Web Token (JWT) Work?

# A JSON Web Token (JWT) is a secure way of transmitting information between two 
# parties — often used in authentication systems. When a user successfully logs into an
#  application using their credentials, the server generates a JWT and sends it back to 
# the client. This token is digitally signed using a secret key (or a private key in
#  asymmetric systems) to ensure the data hasn’t been tampered with. The client stores
#  this token (commonly in local storage or a cookie) and includes it in future requests
# , usually in the Authorization header as Bearer <token>. The server then validates the
#  JWT using the secret key, ensuring that the request is authentic and hasn't been altered.
#  Importantly, all communication should happen over HTTPS to prevent token 
# interception.

import jwt
import datetime

# Secret key used for signing the JWT
SECRET_KEY = "my_super_secret_key"

# Step 1: Create some user data (claims) to encode
payload = {
    "user_id": 42,
    "username": "giton",
    "role": "admin",
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)  # expires in 30 seconds
}

# Step 2: Encode the payload into a JWT
token = jwt.encode(payload, SECRET_KEY, algorithm="HS256")
print("🔐 Encoded JWT Token:")
print(token)

# Step 3: Decode the token to get the original data
try:
    decoded_data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
    print("\n✅ Decoded Payload:")
    print(decoded_data)
except jwt.ExpiredSignatureError:
    print("\n⛔ Token has expired!")
except jwt.InvalidTokenError as e:
    print(f"\n⛔ Invalid token! Error: {e}")

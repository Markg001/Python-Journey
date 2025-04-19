# Notes on Working with PyJWT

# PyJWT is a Python library that enables encoding and decoding of data using the JWT 
# (JSON Web Token) standard. It's useful for securely transmitting information between 
# parties as a JSON object. JWTs are digitally signed using a secret or a public/private
#  key pair. In PyJWT, the encode() function creates a JWT by taking a payload 
# (usually a dictionary), a secret key, and an optional algorithm (default is HS256). 
# The decode() function retrieves the original payload from the token using the same secret 
# key and algorithm. If the key or algorithm doesn't match, or if the token is expired 
# (based on the optional exp field), decoding fails with an appropriate error. 
# This makes JWTs ideal for stateless authentication systems in web apps or APIs.

import datetime
import jwt

SECRET_KEY = "python_jwt"

# Payload with optional expiration (token already expired for demo)
json_data = {
    "sender": "Python JWT",
    "message": "Testing Python JWT",
    "date": str(datetime.datetime.now()),
    "exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=60)  # valid for 60 seconds
}

# Encode the token
encoded_token = jwt.encode(payload=json_data, key=SECRET_KEY, algorithm="HS256")
print("Token:", encoded_token)

# Decode the token
try:
    decoded_data = jwt.decode(jwt=encoded_token, key=SECRET_KEY, algorithms=["HS256"])
    print("Decoded data:", decoded_data)
except Exception as e:
    print({"message": f"Token is invalid --> {e}"})

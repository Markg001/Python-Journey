# Imagine you want to log in to a website using your Google account instead of creating 
# a new username and password. OAuth 2.0 is the system that makes this possible safely.
# It lets one site (like Spotify) access certain information from another site (like your Google profile), 
# without giving away your Google password.

# OAuth 2.0 is a secure way for applications to access a user's data without needing their 
#     password. It works by assigning specific roles to different parts of the process. 
# First, there's the Resource Owner, usually the user, who decides which app can access '
# 'their information and what it can do. The Client is the application that wants access '
# 'to the user's data, like a third-party app. Then there’s the Resource Server, which stores
# the user's data, and finally, the Authorization Server, which confirms the user's identity 
# and gives the client app a special code or token if permission is granted. The process 
# typically begins with the client asking for permission. If the user agrees, the client 
# gets an authorization code, which it sends to the authorization server to get an access 
# token. This token is then used to request the actual data from the resource server. OAuth 
# defines several types of authorization flows depending on how the client and user 
# interact—for example, the Authorization Code flow is used for web apps, while Client 
# Credentials are used when no user data is involved. If the token is valid and everything 
# checks out, the app gets access to the data. If not, access is denied

# This Python script demonstrates how to use OAuth 2.0 to authenticate users with their GitHub 
#     accounts using the requests-oauthlib module. First, the application redirects the user 
#     to GitHub’s login and authorization page. After the user authorizes access, GitHub 
#     redirects them back to the application with a special code. The script captures this 
#     code and exchanges it for an access token. Using this token, the script sends an 
#     authenticated request to GitHub’s API to retrieve the user’s profile information. 
#     This approach allows applications to securely access user data without ever needing 
#     their password, following the OAuth 2.0 Authorization Code Flow.

from requests_oauthlib import OAuth2Session
import json
import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'

from requests_oauthlib import OAuth2Session
import json

# Your GitHub credentials
client_id = 'Ov23lixw68K1KwOFTiWo'
client_secret = 'd88e4ee7a69677c401129bce71645fc16ab0d944'
...

# GitHub app credentials
client_id = 'Ov23lixw68K1KwOFTiWo'
client_secret = 'd88e4ee7a69677c401129bce71645fc16ab0d944'
authorization_base_url = 'https://github.com/login/oauth/authorize'
token_url = 'https://github.com/login/oauth/access_token'

# Step 1: Redirect user to GitHub to authorize
github = OAuth2Session(client_id)
authorization_url, state = github.authorization_url(authorization_base_url)
print("Go to this URL and authorize:", authorization_url)
print("State to remember:", state)  # <- Print the state

# Step 2: After authorization, GitHub redirects to your callback URL with a code
redirect_response = input("Paste the full redirect URL here: ")

# Step 3: Recreate the session with the same state
github = OAuth2Session(client_id, state=state)

# Step 4: Fetch the access token using the code
github.fetch_token(token_url, client_secret=client_secret,
                   authorization_response=redirect_response)

# Step 5: Use the access token to access protected resources (user profile)
response = github.get('https://api.github.com/user')
user_data = json.loads(response.content.decode())

for key, value in user_data.items():
    print(f"{key} --> {value}")


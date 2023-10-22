from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Replace with your Facebook App credentials
FACEBOOK_APP_ID = '629877479344122'
FACEBOOK_APP_SECRET = 'd0b1cb6d60ea7d1b115dfd7594f3680b'
FACEBOOK_REDIRECT_URI = 'https://nextjs-flask-starter.vercel.app/'

# This endpoint initiates the Facebook OAuth process
@app.route('/api/authenticate')
def authenticate():
    facebook_auth_url = f'https://www.facebook.com/v11.0/dialog/oauth?client_id={FACEBOOK_APP_ID}&redirect_uri={FACEBOOK_REDIRECT_URI}&scope=user_friends&response_type=code'
    return facebook_auth_url

# This endpoint handles the Facebook callback
@app.route('/api/auth-callback')
def auth_callback():
    code = request.args.get('code')
    if code:
        # Exchange the code for an access token
        response = requests.get(f'https://graph.facebook.com/v11.0/oauth/access_token?client_id={FACEBOOK_APP_ID}&redirect_uri={FACEBOOK_REDIRECT_URI}&client_secret={FACEBOOK_APP_SECRET}&code={code}')
        data = response.json()
        access_token = data.get('access_token')

        # Use the access token to fetch the user's friend list
        friend_list_response = requests.get(f'https://graph.facebook.com/v11.0/me/friends?access_token={access_token}')
        friend_list = friend_list_response.json()

        return jsonify(friend_list)
    return 'Authentication failed.'

if __name__ == '__main__':
    app.run()

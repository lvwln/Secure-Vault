from flask import Flask, request, jsonify
import jwt
import datetime
import hmac
import hashlib
import struct
import time
from logic import recursive_search

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_super_secret_dev_key' # In production, use environment variables

# Mock Database
USERS = {
    "ninja@example.com": {"secret": "NINJA_HENNGE_SECRET_KEY_001", "role": "admin"}
}

def generate_totp_10_digit(secret):
    """The custom 10-digit SHA-512 logic from HENNGE Mission 3."""
    time_step = 30
    current_time = int(time.time() // time_step)
    msg = struct.pack(">Q", current_time)
    h = hmac.new(secret.encode('ascii'), msg, hashlib.sha512).digest()
    offset = h[-1] & 0x0f
    truncated_hash = struct.unpack(">I", h[offset:offset+4])[0] & 0x7fffffff
    return str(truncated_hash % (10**10)).zfill(10)

@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    user_otp = data.get('otp')

    if email not in USERS:
        return jsonify({"message": "User not found"}), 404

    # Verify using our custom HENNGE-style TOTP
    expected_otp = generate_totp_10_digit(USERS[email]['secret'] + "HENNGECHALLENGE004")
    
    if user_otp == expected_otp:
        # Create a JWT Token valid for 30 minutes
        token = jwt.encode({
            'user': email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)
        }, app.config['SECRET_KEY'], algorithm="HS256")
        
        return jsonify({"token": token, "message": "MFA Verified Successfully!"})
    
    return jsonify({"message": "Invalid TOTP"}), 401

@app.route('/secure-data', methods=['GET'])
def get_data():
    # Example of how we protect a route
    token = request.headers.get('Authorization')
    if not token:
        return jsonify({"message": "Token is missing"}), 403
    try:
        jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        return jsonify({"data": "This is protected data only visible after MFA!"})
    except:
        return jsonify({"message": "Invalid Token"}), 403

if __name__ == '__main__':
    app.run(debug=True)
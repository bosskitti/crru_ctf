import socket
import time

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(('localhost', 8081))
    
    handshake = (
        "GET /ws HTTP/1.1\r\n"
        "Host: localhost:8081\r\n"
        "Upgrade: websocket\r\n"
        "Connection: Upgrade\r\n"
        "Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==\r\n"
        "Sec-WebSocket-Protocol: tty\r\n"
        "Sec-WebSocket-Version: 13\r\n\r\n"
    )
    s.sendall(handshake.encode())
    
    resp = s.recv(4096)
    print("Handshake completed.")
    
    # Send terminal resize frame (which is what ttyd expects first to initialize terminal size)
    # The format is binary frame. But even if we don't, ttyd should spawn the shell.
    # Let's wait 5 seconds
    time.sleep(5)
    
except Exception as e:
    print(f"Error: {e}")

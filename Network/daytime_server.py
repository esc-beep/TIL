import socket
import datetime

HOST = "127.0.0.1"
PORT = 13

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen(1)
    print(f"Daytime server running on {HOST}:{PORT}...")
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S\n")
            conn.sendall(now.encode())

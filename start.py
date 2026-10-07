#!/usr/bin/env python3
import http.server
import os
import socket
import socketserver

START_PORT = 8080
MAX_TRIES = 20


def find_free_port(start=START_PORT):
    for port in range(start, start + MAX_TRIES):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            try:
                sock.bind(("", port))
                return port
            except OSError:
                continue
    raise SystemExit(f"No free port found between {start} and {start + MAX_TRIES - 1}")


def main():
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    port = find_free_port()

    if port != START_PORT:
        print(f"Port {START_PORT} is in use. Using port {port} instead.", flush=True)

    handler = http.server.SimpleHTTPRequestHandler
    with socketserver.TCPServer(("", port), handler) as httpd:
        print(f"Royal Planner site running at http://localhost:{port}", flush=True)
        print("Press Ctrl+C to stop.", flush=True)
        httpd.serve_forever()


if __name__ == "__main__":
    main()

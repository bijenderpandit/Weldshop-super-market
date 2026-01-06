import socket
from weldshop_app_loader import create_app

app = create_app()

if __name__ == "__main__":
    # Get local IP address
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    
    print("\n" + "="*60)
    print("  Fabrication Dashboard is starting...")
    print("="*60)
    print(f"  Local access:    http://127.0.0.1:5000")
    print(f"  Network access:  http://{local_ip}:5000")
    print("="*60)
    print("  Use the Network access URL on other devices")
    print("  (Make sure they're on the same Wi-Fi/network)")
    print("="*60 + "\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)



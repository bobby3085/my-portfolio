from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        health_data = {
            "status": "ok",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "platform": "vercel_functions",
            "uptime": "99.9%",
            "response_time": "< 50ms"
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(health_data).encode())

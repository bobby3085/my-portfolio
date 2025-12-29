from http.server import BaseHTTPRequestHandler
import json
from datetime import datetime

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        response_data = {
            "system_status": "healthy",
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "platform": "vercel_functions",
            "services": {
                "portfolio": {
                    "status": "running",
                    "platform": "vercel",
                    "domain": "prash.shop",
                    "cost": "$0/month"
                },
                "status_api": {
                    "status": "running",
                    "platform": "vercel_functions",
                    "endpoints": ["/api/status", "/api/health"],
                    "cost": "$0/month"
                }
            },
            "hosting": {
                "portfolio": "Vercel (Free Forever)",
                "status_api": "Vercel Functions (Free Forever)",
                "total_cost": "$0/month",
                "previous_cost": "$5/month (Railway)",
                "savings": "100%"
            }
        }
        
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode())

from flask import Flask, request, Response
import requests

app = Flask(__name__)

@app.route('/proxy')
def proxy():
    url = request.args.get('url')
    if not url:
        return "URL parameter is required", 400
    try:
        response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
        return Response(response.content, status=response.status_code, content_type=response.headers['Content-Type'])
    except requests.RequestException:
        return "Error fetching the URL", 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

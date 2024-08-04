from flask import Flask, jsonify
import requests

app = Flask(__name__)

urls_to_check = {
    "youtube": "https://youtube.com",
    "GitHub": "https://github.com",
    "Google": "https://google.com",
    "localUrl": "https://10.com"
}

@app.route('/check_urls', methods=['GET'])
def check_urls():
    results = {}
    for name, url in urls_to_check.items():
        try:
            response = requests.get(url)
            if response.status_code == 200:
                results[name] = True
            else:
                results[name] = False
        except:
            results[name] = False
    return jsonify(results)

if __name__ == '__main__':
    app.run(debug=True, host= "0.0.0.0",port=2000)

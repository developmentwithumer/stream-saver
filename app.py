from flask import Flask, render_template, request
from downloader import Downloader
import validators

app = Flask(__name__)

@app.route('/')
def home():
    return render_template("index.html", info=None, formats=None, error=None)

@app.route('/download/', methods=['POST'])
def download_video():
    url = request.form.get('url')

    if not url:
        message = "No URL provided."
        return render_template("index.html", message=message)
    
    elif not validators.url(url):
        message = "Not a valid URL."
        return render_template("index.html", message=message)

    elif url:
        data = Downloader(url)
        return render_template("index.html", data=data)

if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=8000)
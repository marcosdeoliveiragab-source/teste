from flask import Flask, request, send_file
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)

@app.route('/baixar')
def baixar():
    url = request.args.get('url')
    opcoes = {
    'format': 'bestaudio/best',
    'outtmpl': 'audio.%(ext)s',
    'cookiefile': 'cookies.txt',
    'extractor_args': {'youtube': ['player_client=android']}
    }
    with yt_dlp.YoutubeDL(opcoes) as ydl:
        info = ydl.extract_info(url, download=True)
        arquivo = ydl.prepare_filename(info)
    return send_file(arquivo, as_attachment=True)

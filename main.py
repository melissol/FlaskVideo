from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__, static_folder='static')


# Compress(app)
# app.config['COMPRESS_COMPRESSION_LEVEL'] = 6


@app.route('/favicon.ico')
def favicon():
    return app.send_static_file('ico/favicon.ico')


@app.route('/video')
def video():
    return render_template('video.html')


@app.route('/video_buff')
def video_buff():
    return render_template('video_buff.html')


@app.route('/video_comp')
def video_comp():
    return render_template('video_buff_comp.html')


if __name__ == '__main__':
    app.run(debug=True)

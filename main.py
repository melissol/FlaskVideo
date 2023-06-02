from flask import Flask, render_template
from flask_compress import Compress

app = Flask(__name__, static_folder='static')
Compress(app)
app.config['COMPRESS_COMPRESSION_LEVEL'] = 9


# @app.route('/')
# def index():
#    return render_template('home.html')


@app.route('/')
def video():
    return render_template('video.html')


@app.route('/video_buffering')
def video_buff():
    return render_template('video_buff.html')


if __name__ == '__main__':
    """ """
    app.run(debug=True)

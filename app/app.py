import threading
import webbrowser

from flask import Flask, jsonify, render_template, request

import drone

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cb')
def calc_cells_barcodes():
    err = request.args.get('err', type=float, default=0.1)
    fill = request.args.get('fill', type=float, default=0.8)
    speed = request.args.get('speed', type=float, default=1.0)
    freq = request.args.get('freq', type=float, default=10.0)

    bc = drone.generate_barcodes(err_prob=err, fill=fill)
    dc = drone.generate_drone_cells_array(drone_speed=speed, freq=freq)
    vb = drone.generate_video_barcode(dc, bc)

    cb = drone.generate_cells_barcodes(vb, dc)

    response = jsonify(
        {'width': 16, 'height': 6, 'sourceBarcodes': bc, 'droneCells': dc, 'videoBarcode': vb, 'cellsBarcodes': cb})
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


if __name__ == '__main__':
    threading.Timer(1.25, lambda: webbrowser.open('http://127.0.0.1:5000/')).start()
    app.run()

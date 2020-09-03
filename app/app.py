from flask import Flask, jsonify, render_template

import drone

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cb')
def calc_cells_barcodes():
    bc = drone.generate_barcodes();
    dc = drone.generate_drone_cells_array()
    vb = drone.generate_video_barcode(dc, bc)

    cb = drone.generate_cells_barcodes(vb, dc)

    return jsonify(
        {'width': 16, 'height': 6, 'sourceBarcodes': bc, 'droneCells': dc, 'videoBarcode': vb, 'cellsBarcodes': cb})


if __name__ == '__main__':
    app.run()
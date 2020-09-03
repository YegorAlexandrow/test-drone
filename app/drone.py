import numpy as np


def generate_barcodes():
    bc = [[[s * 100 + l] if np.random.randint(100) < 80 else [] for s in range(16)] for l in range(0, 6)]

    q = np.random.randint(100, size=(6, 16))

    count = 0

    for l in range(1, 6):
        for s in range(16):
            if len(bc[l][s]) == 1 and q[l][s] < 10:
                count = count + 1
                if s == 0 and len(bc[l][s + 1]) == 1:
                    bc[l][s].extend(bc[l][s + 1].copy())
                elif s == 15 and len(bc[l][s - 1]) == 1:
                    bc[l][s].extend(bc[l][s - 1].copy())
                else:
                    tmp = bc[l][s + 1] if q[l][s + 1] * len(bc[l][s + 1]) % 2 > q[l][s - 1] * len(bc[l][s - 1]) % 2 else \
                        bc[l][s - 1]
                    bc[l][s].extend(tmp.copy())

    return bc


def generate_drone_cells_array():
    freq = 10
    drone_speed = 1.0

    dc = []

    dc.extend([(int(l / 2), 0) for l in np.arange(0, 1.9, drone_speed / freq)])

    for s in range(16):
        if s % 2 == 0:
            for l in np.arange(2, 11.9, drone_speed / freq):
                dc.append((int(l / 2), s))
        else:
            for l in np.arange(11.9, 2.0, -drone_speed / freq):
                dc.append((int(l / 2), s))

    dc.extend([(int(l / 2), 15) for l in np.arange(2, 0, -drone_speed / freq)])

    return dc


def generate_video_barcode(cells, barcodes):
    return [barcodes[cell[0]][cell[1]] for cell in cells]


def generate_cells_barcodes(vb, dc):
    cb = [[set() for s in range(16)] for l in range(6)]

    for t in range(len(vb)):
        cb[dc[t][0]][dc[t][1]] |= set(vb[t])

    for l in range(6):
        for s in range(16):
            if len(cb[l][s]) > 1:
                for barcode in cb[l][s]:
                    if (s > 0 and barcode in cb[l][s - 1]) or (s < 15 and barcode in cb[l][s + 1]):
                        cb[l][s].remove(barcode)
                        break

            cb[l][s] = list(cb[l][s])

    return cb
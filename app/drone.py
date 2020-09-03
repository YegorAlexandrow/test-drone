import numpy as np
from random import random


def _rnd(p):
    return random() < p


def generate_barcodes(err_prob=0.1, fill=0.8):
    bc = [[[s * 100000 + l] if l > 0 and _rnd(fill) else [] for s in range(16)] for l in range(6)]

    for l in range(1, 6):
        for s in range(16):
            if len(bc[l][s]) == 1 and _rnd(err_prob):
                if s == 0:
                    if len(bc[l][s + 1]) == 1: bc[l][s].extend(bc[l][s + 1].copy())
                elif s == 15:
                    if len(bc[l][s - 1]) == 1: bc[l][s].extend(bc[l][s - 1].copy())
                else:
                    prior = 1 if _rnd(0.5) else -1

                    if len(bc[l][s + prior]) == 1:
                        bc[l][s].extend(bc[l][s + prior].copy())
                    elif len(bc[l][s - prior]) == 1:
                        bc[l][s].extend(bc[l][s - prior].copy())
    return bc


def generate_drone_cells_array(freq=10.0, drone_speed=1.0):
    dt = drone_speed / freq

    dc = [(int(l / 2), 0) for l in np.arange(0, 2 - dt, dt)]

    for s in range(16):
        if s % 2 == 0:
            for l in np.arange(2, 12 - dt, dt):
                dc.append((int(l / 2), s))
        else:
            for l in np.arange(12 - dt, 2.0, -dt):
                dc.append((int(l / 2), s))

    dc.extend([(int(l / 2), 15) for l in np.arange(2, 0, -dt)])

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

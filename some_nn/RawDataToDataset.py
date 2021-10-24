import argparse
import os
import pickle

import numpy as np

from RawDataOperation import RawDataReader


def readAll(dir):
    for root, dr, files in os.walk(dir):

        g_data = np.empty(shape=(len(files), 8, 2000))
        g_label = np.empty(shape=(len(files)))

        i = 0
        for file in files:

            path = dir + '\\' + file
            data = RawDataReader(fname=path).read()

            with open(path, 'rb') as f:
                g_data[i] = np.array(data).reshape((len(data) // 8, 8)).transpose()
                g_label[i] = 0 if "turn_left" in os.path.splitext(file)[0] else 1
                i = 1 + i

        data = {
            "data": g_data,
            "labels": g_label
        }

        with open("data.pickle", "wb") as f:
            pickle.dump(data, f)

        with open("data.pickle", "rb") as f:
            return pickle.load(f)


parser = argparse.ArgumentParser(description='Raw Data to  Dataset')
parser.add_argument('file', type=str, metavar='path',
                    help='dir for a raw data')
args = parser.parse_args()

readAll(args.file)

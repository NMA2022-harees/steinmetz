from typing import Callable, Dict
import numpy as np
import os
import requests


def fetch_data_if_not_exist(file_name: str, url: str):
    """
    Fetch data from a URL and return it as a string.
    """
    if not os.path.exists(file_name):
        try:
            r = requests.get(url)
        except requests.ConnectionError:
            print("!!! Failed to download data !!!")
        else:
            if r.status_code != requests.codes.ok:
                return print("!!! Failed to download data !!!")
            with open(file_name, "wb") as fd:
                fd.write(r.content)
    return


def split_data_into_each_contrast_pairs(alldata: np.ndarray, key: str, callback: Callable = lambda arr: arr) -> Dict[tuple, np.ndarray]:
    d = dict()
    for data in alldata:
        values = np.array(callback(data[key]))
        pairs = list(zip(data["contrast_left"], data["contrast_right"]))
        n_trials = len(pairs)
        for i in range(n_trials):
            d[pairs[i]] = np.append(d.setdefault(pairs[i], np.array([])), values[i])
    return d

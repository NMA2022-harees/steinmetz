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

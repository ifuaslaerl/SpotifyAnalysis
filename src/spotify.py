import os
import pandas as pd

from src.account import AccountData
from src.extended import ExtendedData

class SpotifyData:

    def __init__(self, path: str):
        assert os.path.exists(path)
        self.path: str = path

        self.account = AccountData(os.path.join(path, 
                                "Spotify Account Data"))
        self.extended = ExtendedData(os.path.join(path,
                    "Spotify Extended Streaming History"))

if __name__ == "__main__":
    spotify_data = SpotifyData("data/personal_data/my_spotify_data")
import os
import pandas as pd

class ExtendedData:

    def __init__(self, path: str):
        assert os.path.exists(path)
        self.path: str = path

if __name__ == "__main__":
    pass
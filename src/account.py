import os
import typing
import pandas as pd

class AccountData:

    def __init__(self, path: str):
        assert os.path.exists(path)
        self.path: str = path

        # self.data: typing.Dict[str, pd.DataFrame] = \

if __name__ == "__main__":
    pass
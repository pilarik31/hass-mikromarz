import os.path
from pathlib import Path
import json
import logging

class Config():

    def __init__(self) -> None:
        self._LOGGER = logging.getLogger(__name__)
        self.file_path = str(Path(__file__).resolve().parent) + "/config.json"
        self._LOGGER.warning(self.file_path)
        if not os.path.isfile(self.file_path):
            with open(self.file_path, 'w') as f:
                f.write(
                    json.dumps(
                        {
                            "url": "0.0.0.0"
                        },
                        sort_keys=True,
                        indent=4,
                        separators=(',', ': ')
                    )
                )
        

    def set(self, key: str, value: str) -> None:
        with open(self.file_path, "r", encoding='utf-8') as f:
            data = json.load(f)

        data[key] = value

        with open(self.file_path, "w") as f:
            f.write(
                json.dumps(
                    data,
                    sort_keys=True,
                    indent=4,
                    separators=(',', ': ')
                )
            )

    def get(self, key: str) -> str|int:
        with open(self.file_path, "r") as f:
            data = json.loads(f.read())

        return data[key]


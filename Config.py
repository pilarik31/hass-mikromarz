import json

class Config():
    def set(key: str, value: str) -> None:
        with open("config.json", "r") as f:
            data = json.loads(f.read())

        data[key] = value

        with open("config.json", "w") as f:
            f.write(
                json.dumps(
                    data,
                    sort_keys=True,
                    indent=4,
                    separators=(',', ': ')
                )
            )

    def get(key: str) -> str|int:
        with open("config.json", "r") as f:
            data = json.loads(f.read())

        return data[key]


import json


def load_data(path: str) -> list[dict]:
    """
    Load data from the given path and return it as a list of dictionaries.
    """

    with open(path, "r") as file:
        contents = file.read()
        data = json.loads(contents)

        return data

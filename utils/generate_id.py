_id = 0


def generate_id() -> int:
    """
    Generate a unique ID.

    Returns:
    int: A unique ID incremented by 1 every time this function is called.
    """

    global _id
    _id += 1
    return _id

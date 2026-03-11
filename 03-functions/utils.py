def car_detail(**car_info):
    """
    Summarizes car specifications in to a readable string.
    Args:
    **car_info: keyword arguments representing car attributes
    returns:
           str: A formatted summary of the car.
    """
    model = car_info.get("model", "unknown")
    color = car_info.get("color", "unspecified color")
    transmission = car_info.get("transmission", "standard")
    return f"Car summary: {model} | {color} | {transmission} transmission"

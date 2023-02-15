__all__ = ["route"]


def route(pathname: str):
    def decorator(obj):
        setattr(obj, "pathname", pathname)
        return obj

    return decorator

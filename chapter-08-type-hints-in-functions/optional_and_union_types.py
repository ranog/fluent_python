# from typing import Optional

# def show_count(count: int, singular: str, plural: Optional[str] = None) -> str:   # before
def show_count(count: int, singular: str, plural: str | None = None) -> str:        # after > Python 3.10
    ...

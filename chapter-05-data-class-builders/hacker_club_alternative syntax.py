from dataclasses import dataclass


@dataclass
class HackerClubMember:
    .name: str                                      # (1)
    .guests: list = field(default_factory=list)
    .handle: str = ''

    all_handles = set()                             # (2)

# 1 - Instance attributes must be declared with a . prefix.
# 2 - Any attribute name that doesn't have a . prefix is a class attribute (as they always have been).

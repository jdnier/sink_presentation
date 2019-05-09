"""
Human units helpers.

There's an old humanize package but it's not being maintained.

"""

from typing import Optional

from .pairwise import pairwise


_labels = ('B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB', 'EiB', 'ZiB', 'YiB')
_labels_sizes = ((1024**i, label) for i, label in enumerate(_labels))
_SIZE_RANGES = list(pairwise(_labels_sizes))

_DEFAULT_PRECISION = 2
_DEFAULT_PRECISION_EXCEPTIONS = {'B': 0, 'KiB': 1}


def humanize_bytes(num_bytes: int, precision: Optional[int] = None) -> str:
    abs_bytes = abs(num_bytes)
    for (size, label), (next_size, next_label) in _SIZE_RANGES:
        if abs_bytes <= next_size:
            break
    human_bytes = num_bytes / size
    if precision is None:
        precision = _DEFAULT_PRECISION_EXCEPTIONS.get(label, _DEFAULT_PRECISION)
    return f'{human_bytes:.{precision}f} {label}'


__all__ = ['humanize_bytes']

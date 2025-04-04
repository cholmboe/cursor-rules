#!/usr/bin/env python3

"""
This script ensures all files in the rules directory have the same suffix (.md or .mdc)
Usage: ./toggle_extensions.py [md|mdc]
If no argument is provided, it will detect the most common suffix and use the opposite
"""

import os
import sys
from pathlib import Path
from collections import Counter
from typing import Final

VALID_SUFFIXES: Final[frozenset[str]] = frozenset(['md', 'mdc'])

def get_target_suffix() -> str:
    """Determine target suffix (opposite of most common)"""
    rules_dir = Path(__file__).parent / 'rules'
    suffix_counts = Counter(
        f.suffix[1:] for f in rules_dir.glob('*.*')
        if f.is_file() and f.suffix[1:] in VALID_SUFFIXES
    )
    return 'mdc' if suffix_counts['md'] > suffix_counts['mdc'] else 'md'

def ensure_suffix(target_suffix: str) -> None:
    """Ensure all files have the target suffix."""
    if target_suffix not in VALID_SUFFIXES:
        raise ValueError(f"Invalid suffix: {target_suffix}")

    rules_dir = Path(__file__).parent / 'rules'
    for file in rules_dir.glob('*.*'):
        if not file.is_file():
            continue
        current_suffix = file.suffix[1:]
        if current_suffix in VALID_SUFFIXES and current_suffix != target_suffix:
            file.rename(file.with_suffix(f'.{target_suffix}'))

def main() -> None:
    """Main function to toggle extensions."""
    try:
        if len(sys.argv) > 1:
            suffix = sys.argv[1].lower()
            if suffix not in VALID_SUFFIXES:
                sys.exit("Error: Suffix must be either 'md' or 'mdc'")
            target_suffix = suffix
        else:
            target_suffix = get_target_suffix()

        os.chdir(Path(__file__).parent)
        ensure_suffix(target_suffix)
        print(f"All rules files now have .{target_suffix} suffix")
    except (OSError, ValueError) as e:
        sys.exit(f"Error: {str(e)}")

if __name__ == '__main__':
    main()

# Cursor Rules

My Cursor rules repository.

## How to use

Link your project's `.cursor/rules` to this repo's `rules` directory.

## Utility script: toggle_extensions.py

Cursor Agent is reluctant to edit .mdc files directly, likely for safety reasons. Use this script to conveniently change suffixes while crafting rules.

Usage:

```bash
# To change all rule files to .md suffix
./toggle_extensions.py md

# To change all rule files to .mdc suffix
./toggle_extensions.py mdc

# To automatically toggle to the opposite of the most common suffix
./toggle_extensions.py
````

## Credits

<https://github.com/PatrickJS/awesome-cursorrules>

# Cursor Rules

My Cursor rules repository.

## How to use

Link your project's `.cursor/rules` to this repo's `rules` directory.

You can add the something like this in your user rules (in Cursor settings -> Rules) to get cursor to help out:

```
- If `.cursor/rules` directory does not exist in the current project, suggest linking it to a global rules directory
   Use the following command to set up the link: 'mkdir -p .cursor && ln -s ~/src/github.com/cholmboe/cursor-rules/rules .cursor/rules'
```

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

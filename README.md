# Sublime Junk
Some helper for use with Sublime Text


## Setup - Package Control
- `cmd+shift+p` and then select "Package Control: Add Repository"
- add `https://github.com/prime31/Sublime-Text-Junk`
- `cmd+shift+p` "Package Control: Install Package" and choose the `Sublime Text Junk` package

## Setup - Manual
- open your Sublime Text package folder (`Sublime Text -> Preferences -> Browse Packages` menu item)
- `git clone hhttps://github.com/prime31/Sublime-Text-Junk


## What Do You Get?
- right-click with a word selected and there is a `Text Transformations` menu
- right-click in the project pane for `open in iTerm`, `Duplicate` and `Move` commands
- automatic handling of opening/closing the minimap and sidebar when opening/closing Origami panes
- `Multi command plugin` to allow creating keyboard shortcuts/commands that chain together multiple Sublime commands

Some examples:
```
	{
		// fix unused variable
		"keys": ["super+shift+m"],
		"command": "multicommand",
		"args": {
			"commands": [
				{ "command": "find_under_expand" },
				{ "command": "copy" },
				{ "command": "move_to", "args": {"to": "eol"} },
				{ "command": "insert", "args": {"characters": "\n"} },
				{ "command": "insert", "args": {"characters": "_ = "} },
				{ "command": "paste" },
				{ "command": "insert", "args": {"characters": ";"} },
			]
		}
	},
	{
		// fix unused function parameter
		"keys": ["super+shift+n"],
		"command": "multicommand",
		"args": {
			"commands": [
				{ "command": "find_under_expand" },
				{ "command": "copy" },
				{ "command": "move_to", "args": {"to": "brackets"} },
				{ "command": "move_to", "args": {"to": "eol"} },
				{ "command": "insert", "args": {"characters": "\n"} },
				{ "command": "insert", "args": {"characters": "_ = "} },
				{ "command": "paste" },
				{ "command": "insert", "args": {"characters": ";"} },
			]
		}
	}
```

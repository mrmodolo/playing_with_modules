# Structuring Your Project
https://docs.python-guide.org/writing/structure/

## Mars
https://en.wikipedia.org/wiki/Mars

# Untrack files already added to git repository based on .gitignore
http://www.codeblocq.com/2016/01/Untrack-files-already-added-to-git-repository-based-on-gitignore/

```git
git rm -r --cached .
git add .
git commit -m ".gitignore fix"
```

# Available Layers » git
https://spacevim.org/layers/git/

# Available Layers » python
https://spacevim.org/layers/lang/python/#install
Install
enable layer
To use this configuration layer, add following snippet to your custom configuration file.

```toml
[[layers]]
  name = "lang#python"
language tools
syntax checking:
```

checker layer provide syntax checking feature, and for Python it uses flake8 package:

pip install --user flake8

code formatting:

The default key binding for formatting buffer is SPC b f, and you need to install yapf. To enable automatic buffer formatting on save, load this layer with setting format_on_save to 1.

```toml
[[layers]]
  name = "lang#python"
  format_on_save = 1
```

pip install --user yapf
format imports:

To be able to suppress unused imports easily, install autoflake:

pip install --user autoflake

To be able to sort your imports, install isort

pip install --user isort
code coverage:

To be able to show code coverage, install coverage.py

pip install --user coverage

Configuration
By default, when create a new python file, SpaceVim will insert file head automatically. to change the file head, use python_file_head option:

```toml
[[layers]]
  name = "lang#python"
  python_file_head = [
      '#!/usr/bin/env python',
      '# -*- coding: utf-8 -*-',
      '',
      ''
  ]
```

When enable autocomplete layer, the symbol will be complete automatically. By default the type info is disabled, because it is too slow. To enable type info:

```toml
[[layers]]
  name = "lang#python"
  enable_typeinfo = true
```

"""
==============
Path variables
==============
"""

from pathlib import Path

# Current directory
pkgdir    = (Path(__file__) / ".." / "..").resolve() # First .. for file name, second .. for utils path

# Config file path
conf_path = pkgdir / "config.toml"

"""
This is a setup.py script generated by py2applet

Usage:
    python3 setup.py py2app
"""

from setuptools import setup

APP = ['HOME.py']
DATA_FILES = []  # for text files
OPTIONS = {
    'iconfile':'cold_call.icns',
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)

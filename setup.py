from setuptools import setup

APP = ['shelby_encryptor.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': False,
    'packages': ['tkinter'],
    'includes': [
        'pkg_resources',
        'jaraco',
        'jaraco.text',
        '_cffi_backend',
        'cryptography.hazmat.bindings._rust'
    ],
    'iconfile': None,  # Optional: replace with 'youricon.icns' if you have one
    'plist': {
        'CFBundleName': 'ShelbyEncryptor',
        'CFBundleDisplayName': 'ShelbyEncryptor',
        'CFBundleIdentifier': 'com.shelby.encryptor',
        'CFBundleVersion': '1.0.0',
        'LSUIElement': False,  # Set True to hide dock icon
    },
}

setup(
    app=APP,
    name='ShelbyEncryptor',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)


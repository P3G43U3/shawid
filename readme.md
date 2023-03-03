# Simple HWID Auth

This is a authentification for your [Python](https://www.python.org/) projects. It uses my [Shacrypt](https://github.com/64biit/sha256-encryption) library for encrypting the hardware-ids. The hwids are stored on [Pastebin](https://pastebin.com), where you can easily add and remove the hwids, giving you full control of your software at any time.

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install.

```bash
pip install requests shacrypt pasteid
```

## Usage

```python
import pasteid

# use it
pasteid.auth("your_pastebin_code", "your_contact")
```

## Get Pastebin Code
![alt(]https://raw.githubusercontent.com/64biit/hwid-auth/main/pastebin.png)
---

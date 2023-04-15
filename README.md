# Py Github GUI
A simple graphical user interface for receiving public details of a GitHub profile.

![animatedshowcase](https://user-images.githubusercontent.com/42397332/232237031-ab5060d4-5d46-4781-97b4-eafb163f8919.gif)

![Current Version](https://img.shields.io/badge/version-v1.1.1-blue)
![GitHub stars](https://img.shields.io/github/stars/rackodo/py-github-gui?style=social)
![GitHub forks](https://img.shields.io/github/forks/rackodo/py-github-gui?style=social)
![Twitter Follow](https://img.shields.io/twitter/follow/rackodo?style=social)

## Table of Contents
- [Getting Started](#getting-started)
	- [Tools Required](#tools-required)
	- [Installation](#installation)
	- [Using](#using)
- [Authors](#authors)
- [Thanks](#thanks)
- [License](#license)

## Getting Started

### Tools Required

* PIP
* A correctly configured Python environment for Tkinter.

### Installation

In a command line, run these commands:
```bash
$ python3 -m pip install --upgrade pip 
```
```bash
$ python3 -m pip install py-github-gui-rackodo
```
The second command should install Py Github GUI and all of its necessary dependencies.

### Using

To use Py Github GUI, you'll first need a Github Personal Access Token. Here's how to get one:
1. Navigate to Github's settings page and scroll down to `Developer Settings`.
2. Click on `Personal Access Tokens`, then `Tokens (Classic)`.
3. Click on `Generate New Token`, then `Generate New Token (Classic)`. Verify your password if necessary.
4. Name the token whatever you'd like, give it an expiry date however you see fit, and then scroll down to check the box next to `read:user`.
5. Generate the token, and save it in a text file so you don't lose it.

Now, to actually use Py Github GUI, run **this** command:
```bash
$ python3 -m py_github_gui ghp_yourgeneratedtoken12345
```

In the opened window, type the username of a GitHub user and press the `Get Information` button. The available information will be shown.

## Authors

#### Bash Elliott
* [GitHub]

## Thanks
* [@aottr](https://github.com/aottr) and [@craftzdog](https://github.com/craftzdog)

## License

`py-github-gui` is open source software [licensed as MIT][license].

[//]: # (HyperLinks)


[GitHub]: https://github.com/rackodo

[license]: https://github.com/rackodo/py-github-gui/blob/main/LICENSE.md
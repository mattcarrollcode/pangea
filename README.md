# Pangea API usage

## Setup

Note: this setup has only been testing for macOS.

### Python

1. clone this repo and `cd` to the root of the repo
1. Install pyenv and pyenv-virtualenv: `brew install pyenv pyenv-virtualenv`
1. Add the following to your `~/.bashrc` or `~/.zshrc` file:
  ```
  export PYENV_ROOT="$HOME/.pyenv"
  export PATH="$PYENV_ROOT/bin:$PATH"
  eval "$(pyenv init -)"
  eval "$(pyenv virtualenv-init -)"
  ```
1. Ensure your RC file has been run in your current shell: `source ~/.zshrc` or `source ~/.zshrc`
1. install Python version 3.11.2: `pyenv install 3.11.2`
1. Create a new virtual enviornemtn: `pyenv virtualenv 3.11.2 pangea`
1. Link the virutal enviornemtn to the repo: `pyenv local pangea`
1. Ensure you are using the enviornment you just created:`pyenv which python` you should see something like: `.pyenv/versions/pangea/bin/python`. if you don't see `pangea` somewhere in the path, you've made a mistake somewhere

### Dependencies

1. `pip install -r requriements.txt`

## Running the code

1. Python `python pangea.py`
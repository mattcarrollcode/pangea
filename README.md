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
1. `pip install -r requriements.txt`

### Pangea

1. Create a Pangea account: https://pangea.cloud/docs/admin-guide/getting-started/create-account/
1. Login to Pangea console
1. Go to the Tokens page: https://console.pangea.cloud/project/tokens and click on the the "Create" button in the upper right hand corner
1. Enter a name for the token and click the box labeled `IP Intel`
   ![pangea console token creation page](https://raw.githubusercontent.com/mattcarrollcode/pangea/main/console-create-a-token.png) then click the `Create token` button
1. Next, in the list of tokens, click the copy symbole on the token you just created and paste it in the `.env` file in the repo in plac eof `CHANGE_ME` for the value of `PANGEA_INTEL_TOKEN`

## Running the code

1. Run `python pangea-ip-intel-example.py`
   You should see similar output to what is below:
   ```
   $ python pangea-ip-intel-example.py
   Calling Pangea IP Intel Geolocate API with IP Address '93.231.182.110'...
   Data:
   {   'city': 'unna',
       'country': 'Federal Republic Of Germany',
       'country_code': 'de',
       'latitude': 51.56,
       'longitude': 7.65,
       'postal_code': '59425'}
   Raw Data:
   {   'area_codes': '?',
       'city': 'unna',
       'city_code': 7627,
       'city_conf': 95,
       'connection_speed': 'xdsl',
       'connection_type': 'wifi',
       'continent_code': 5,
       'country': 'deu',
       'country_code': 276,
       'country_conf': 99,
       'gmt_offset': 200,
       'in_dst': 'y',
       'internal_code': 24,
       'latitude': 51.56,
       'longitude': 7.65,
       'max_ip': '93.231.182.111',
       'metro_code': 276002,
       'min_ip': '93.231.182.104',
       'postal_code': '59425',
       'postal_conf': 90,
       'region': 'nw',
       'region_code': 10528,
       'region_conf': 99,
       'timezone_name': 'europe/berlin',
       'two_letter_country': 'de'}
   ```


from pprint import pprint

import pangea.exceptions as pe
from pangea.config import PangeaConfig
from pangea.services import IpIntel

from dotenv import dotenv_values

class PangeaClient:
  def __init__(self, domain: str, token:str):
    self.domain = domain
    self.token = token
    # Create IP Intel client to call IP Intel APIs
    self.intel = IpIntel(token, config=PangeaConfig(domain=domain))

  def geolocate(self, ip_addr: str):
    try:
        response = self.intel.geolocate(ip=ip_addr, provider="digitalelement", verbose=True, raw=True)
        data = response.result.raw_data.copy()
        data['country_name'] = response.result.data.country
        return data
    except pe.PangeaAPIException as e:
        print(f"Request Error: {e.response.summary}")
        for err in e.errors:
            pprint(f"\t{err.detail} \n", indent=4)
        exit(1)

if __name__ == "__main__":
  # Get values from local .env file
  config = dotenv_values(".env")
  
  # Use token and domain from .env file
  domain = config["PANGEA_DOMAIN"]
  token = config["PANGEA_INTEL_TOKEN"]
  # Thrown an error if the token or domain wasn't set up
  if token == "CHANGE_ME" or domain == "CHANGE_ME":
    print("Please update the `.env` file with the PANGEA_INTEL_TOKEN and/or PANGEA_DOMAIN from your Pangea account. See README.md for more info.")
    exit(1)

  client = PangeaClient(domain, token)
  ip_addr = "93.231.182.110"
  print(f"Calling Pangea IP Intel Geolocate API with IP Address '{ip_addr}'...")
  ip_info = client.geolocate(ip_addr)
  pprint(ip_info, indent=4)

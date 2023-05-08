from pprint import pprint

import pangea.exceptions as pe
from pangea.config import PangeaConfig
from pangea.services import IpIntel

from dotenv import dotenv_values

def geolocate(ip_addr: str, token: str, domain: str):
  print(f"Calling Pangea IP Intel Geolocate API with IP Address '{ip_addr}'...")
  config = PangeaConfig(domain=domain)
  intel = IpIntel(token, config=config)
  try:
      response = intel.geolocate(ip=ip_addr, provider="digitalelement", verbose=True, raw=True)
      print("Data:")
      pprint(dict(response.result.data), indent=4)
      print("Raw Data:")
      pprint(response.result.raw_data, indent=4)
  except pe.PangeaAPIException as e:
      print(f"Request Error: {e.response.summary}")
      for err in e.errors:
          pprint(f"\t{err.detail} \n", indent=4)

if __name__ == "__main__":
  # Get values from local .env file
  config = dotenv_values(".env")
  
  # Use token and domain from .env file
  token = config["PANGEA_INTEL_TOKEN"]
  domain = config["PANGEA_DOMAIN"]
  # Thrown an error if the token or domain wasn't set up
  if token == "CHANGE_ME" or domain == "CHANGE_ME":
    print("Please update the `.env` file with the PANGEA_INTEL_TOKEN and/or PANGEA_DOMAIN from your Pangea account. See README.md for more info.")
    exit(1)

  geolocate("93.231.182.110", token, domain)

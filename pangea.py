from pangea.services import IpIntel

response = intel.geolocate(
  ip="23.129.64.211",
  provider="digitalelement",
  raw=True
)

print(response)
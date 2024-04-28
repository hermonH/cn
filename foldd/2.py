from ipaddress import ip_interface

def get_network_host_id(ip_address):
  """
  This function takes an IP address in CIDR notation and returns the network ID and host ID.

  Args:
      ip_address: The IP address in CIDR notation (e.g., "192.168.1.0/24").

  Returns:
      A tuple containing the network ID and host ID (e.g., ("192.168.1.0", "255.255.255.0")).
  """
  try:
    # Use ipaddress module for safe and efficient IP address handling
    interface = ip_interface(ip_address)
    network_address = interface.network
    host_mask = int(~interface.netmask)  # Invert netmask to get host mask
    host_id = str(ip_interface(address=network_address, mask=host_mask))
    return str(network_address), host_id
  except ValueError:
    return "Invalid IP address or CIDR notation."

# Get user input
ip_address = input("Enter IP address in CIDR notation (e.g., 192.168.1.0/24): ")

# Call the function and print results
network_id, host_id = get_network_host_id(ip_address)
if network_id != "Invalid IP address or CIDR notation.":
  print("Network ID:", network_id)
  print("Host ID:", host_id)
else:
  print(network_id)
from ipaddress import ip_interface
import math
def get_subnet_info(ip_address, num_subnets):
  """
  This function takes an IP address and the desired number of subnets and returns the subnet mask and subnetwork address for each subnet.

  Args:
      ip_address: The IP address in dotted decimal notation (e.g., "192.168.1.0").
      num_subnets: The number of subnets to create.

  Returns:
      A list of dictionaries, where each dictionary contains the subnet mask and subnetwork address for a subnet.
  """
  try:
    # Convert IP address to object for manipulation
    ip_obj = ip_interface(ip_address)
    # Get number of bits needed for subnetting based on number of subnets
    cidr_prefix = 32 - int(round(math.log2(num_subnets + 2)))
    subnet_mask = ip_interface(address="255.255.255.255", mask=cidr_prefix)
    # Calculate usable bits for host addressing
    host_bits = 32 - cidr_prefix

    subnet_info = []
    # Iterate through each subnet address
    for i in range(num_subnets):
      subnet_address = ip_obj.network + (i << host_bits)
      subnet_info.append({"Subnet Mask": str(subnet_mask.netmask), "Subnetwork Address": str(subnet_address)})

    return subnet_info
  except ValueError:
    return "Invalid IP address."

# Get user input
ip_address = input("Enter IP address (e.g., 192.168.1.0): ")
num_subnets = int(input("Enter the number of subnets: "))

# Call the function and print results
subnet_info = get_subnet_info(ip_address, num_subnets)
if subnet_info != "Invalid IP address.":
  for subnet in subnet_info:
    print("Subnet Mask:", subnet["Subnet Mask"])
    print("Subnetwork Address:", subnet["Subnetwork Address"])
    print("---")
else:
  print(subnet_info)
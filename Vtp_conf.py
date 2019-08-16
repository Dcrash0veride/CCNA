import argparse

parser = argparse.ArgumentParser(description="Configure some gear.")
parser.add_argument("--vtp", help="Configure simple vtp", action="store_true")
parser.add_argument("--vlan", help="Configure simple vlans", action="store_true")
parser.add_argument("--port", help="Configure interface to Vlan", action="store_true")
parser.add_argument("--fast", help="Enable portfast on all non-trunking interfaces", action="store_true")
parser.add_argument("--single", help="Enable a port and portfast for a single port", action="store_true")
parser.add_argument("--gateway", help="Define a default gateway", action="store_true")

def vtp_configure():
    a, b, c = input("Please enter the mode, domain, and password: ").split()
    print("en")
    print("conf t")
    print("vtp mode" + " " + a)
    print("vtp domain" + " " + b)
    if c == "None":
        pass
    else:
        print("vtp password " + c)
    if a == "server":
        print("vtp pruning")

def vlan():
    x, y = input("Please enter a vlan ID and name: ").split()
    print("en")
    print("conf t")
    print("vlan" + " " + x)
    print("name" + " " + y)

def port_vlan():
    interface,vlan_number = input("Please enter an interface and a vlan ID: ").split()
    print("This assumes default switchport mode of access and fastethernet!")
    print("en")
    print("conf t")
    if "-" not in str(interface):
        print("interface fastethernet " + interface)
        print("switchport access vlan " + vlan_number)
    elif "-" in str(interface):
        first, last = str(interface).split('-')
        print("interface range fastethernet " + first + " " + "- " + last)
        print("switchport  access vlan "+  vlan_number)

def port_fast():
    mode = input("Please select spanning-tree mode, unless default is desired: ")
    primary, id = input("Please indicate if this device will be root primary/secondary and type in a vlan ID: ").split()
    print("en")
    print("conf t")
    if len(primary) > 0:
        print("spanning-tree vlan " + id + " root " + primary)
    elif len(mode) > 0:
        print("spanning-tree mode " + mode)
    else:
        print("spanning-tree portfast default")

def single_portfast():
    port = input("Which port would you like to enable portfast on? ")
    print("en")
    print("conf t")
    print("interface fastethernet " + port)
    print("spanning-tree portfast")
    print("no shut")

def gateway():
    ipaddr = input("What is the IP address for the gateway? ")
    print("en")
    print("conf t")
    print("ip default-gateway " + ipaddr)



args = parser.parse_args()
if args.vtp:
    vtp_configure()
elif args.vlan:
    vlan()
elif args.port:
    port_vlan()
elif args.fast:
    port_fast()
elif args.single:
    single_portfast()
elif args.gateway:
    gateway()
else:
    pass


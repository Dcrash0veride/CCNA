import argparse

parser = argparse.ArgumentParser(description="Configure some gear.")
parser.add_argument("--vtp", help="Configure simple vtp", action="store_true")
parser.add_argument("--vlan", help="Configure simple vlans", action="store_true")
parser.add_argument("--port", help="Configure interface to Vlan", action="store_true")

def vtp_configure():
    a, b, c = input("Please enter the mode, domain, and password: ").split()
    print("en")
    print("conf t")
    print("vtp mode" + " " + a)
    print("vtp domain" + " " + b)
    print("vtp password" + " " + c)
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


args = parser.parse_args()
if args.vtp:
    vtp_configure()
elif args.vlan:
    vlan()
elif args.port:
    port_vlan()
else:
    pass


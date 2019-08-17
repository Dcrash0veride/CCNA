import argparse

parser = argparse.ArgumentParser(description="Configure some gear.")
parser.add_argument("--vtp", help="Configure simple vtp", action="store_true")
parser.add_argument("--vlan", help="Configure simple vlans", action="store_true")
parser.add_argument("--port", help="Configure interface to Vlan", action="store_true")
parser.add_argument("--fast", help="Enable portfast on all non-trunking interfaces", action="store_true")
parser.add_argument("--single", help="Enable a port and portfast for a single port", action="store_true")
parser.add_argument("--gateway", help="Define a default gateway", action="store_true")
parser.add_argument("--tc", help="Configure channel group", action="store_true")


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


def config_trunk_channel():
    l3 = input("Is this a layer 3 ether channel? y/n: ")
    if l3 == 'y':
        port_channel = input("Please enter the port channel: ")
        ip_add, subnet_mask = input("Please enter the IP address and subnet mask: ").split()
        interfaces = input("Please enter the interfaces: ").split()
        print("en")
        print("conf t")
        print("interface port-channel " + port_channel)
        print("no switchport")
        print("ip address " + ip_add + " " + subnet_mask)
        for i in interfaces:
            print("interface fastethernet " + i)
            print("no switchport")
            print("channel-group " + port_channel + " mode on")
    else:
        channel_protocol, negotiation = input("Please select channel protocol and negotiation: ").split()
        interfaces = input("Please enter the interfaces:  ").split()
        encap, channel_group = input("Please enter the encapsulation type, and channel group: ").split()
        print("en")
        print("conf t")
        print("interface fastethernet " + interfaces[0])
        print("switchport trunk encapsulation " + encap)
        print("switchport mode trunk")
        print("interface fastethernet " + interfaces[1])
        print("switchport trunk encapsulation " + encap)
        print("switchport mode trunk")
        if 'active' in negotiation:
            for i in interfaces:
                print("interface fastethernet " + i)
                print("channel-protocol " + channel_protocol)
                print("channel-group " + channel_group + " mode " + negotiation)
        elif 'passive' in negotiation:
            for i in interfaces:
                print("interface fastethernet " + i)
                print("channel-group " + channel_group + " mode " + negotiation)
        elif len(channel_protocol) > 0 and len(negotiation) > 0:
            for i in interfaces:
                print("interface fastethernet " + i)
                print("channel-protocol " + channel_protocol)
                print("channel-group " + channel_group + " mode " + negotiation)
        elif len(channel_protocol) > 0 and len(negotiation) == 0:
            for i in interfaces:
                print("interface fasthernet " + i)
                print("channel-protocol " + channel_protocol)
                print("channel-group " + channel_group + " mode on")
        elif len(negotiation) > 0 and len(channel_protocol) == 0:
            for i in interfaces:
                print("interface fastethernet " + i)
                print("channel-group " + channel_group + " mode " + negotiation)
        else:
            for i in interfaces:
                print("channel-group " + channel_group + "mode on")
                print("interface fasthethernet " + i)


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
elif args.tc:
    config_trunk_channel()
else:
    pass


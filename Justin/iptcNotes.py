# https://python-iptables.readthedocs.io/en/latest/examples.html

>>> import iptc
>>> rule = iptc.Rule()
>>> rule.in_interface = "eth0"
>>> rule.src = "192.168.1.0/255.255.255.0"
>>> rule.protocol = "tcp"
#create a rule that will match tcp packets coming in on "etc0" with a source IP 
#of 192.168.1.0/255.255.255.0 (192.168.1.0/24)

#A rule may contain matches and a target.
#A match is a filter matching certain packet attributes
#A target tells what to do with the packet (dropt it, accept it, transform it, etc)

#Create a rule that matches tcp packets and drops them:
>>> rule = iptc.Rule()
>>> m = rule.create_match("tcp")
>>> t = rule.create_target("DROP")

#Match and target params can be changed after creation
#it is possible to instantiate them with their constructor but you would still need a rule
#and you have to add matches and the target to their rule manually:
>>> rule.add_match(match)
>>> rule.target = target

#any params match or target might take can be set via the attributes of the obj.
#set the destination port for a tcp match:
>>> rule = iptc.Rule()
>>> rule.protocol = "tcp"
>>> match = rule.create_match("tcp")
>>> match.dport = "80"

#create a rule that matches packets marked with 0xff:
>>> rule = iptc.Rule()
>>> rule.protocol = "tcp"
>>> match = rule.create_match("mark")
>>> match.mark = "0xff"

#parameters are always strings. 
#You can supply any string as a parameter value, however, most extensions validate their parameters

#Certain params may consist of multiple word strings:
>>> rule = iptc.Rule()
>>> rule.src = "127.0.0.1"
>>> rule.protocol = "udp"
>>> rule.target = rule.create_target("ACCEPT")
>>> match = rule.create_match("comment")
>>> match.comment = "this is a test comment" #the "comment" match is a param consisting of multiple words
>>> chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
>>> chain.insert_rule(rule)

#using the "name" attribute, you can print all information of a rule:
>>> for chain in table.chains:
>>>     print "======================="
>>>     print "Chain ", chain.name
>>>     for rule in chain.rules:
>>>         print "Rule", "proto:", rule.protocol, "src:", rule.src, "dst:", \
>>>               rule.dst, "in:", rule.in_interface, "out:", rule.out_interface,
>>>         print "Matches:",
>>>         for match in rule.matches:
>>>             print match.name,
>>>         print "Target:",
>>>         print rule.target.name
>>> print "======================="

#Accessing a table:
>>> table = iptc.Table(iptc.Table.FILTER)
>>> print table.name

#once a table has been initialized, it can be added to:
>>> table = iptc.Table(iptc.Table.FILTER)
>>> chain = table.create_chain("testchain")
#Note that the four fixed tables (FILTER, NAT, MANGLE, RAW) are cached. So if you try to create a new one
#and it has already been instantiated, the creation will be refused.

#Example of rejecting packets from a source address:
>>> import iptc
>>> chain = iptc.Chain(iptc.Table(iptc.Table.FILTER), "INPUT")
>>> rule = iptc.Rule()
>>> rule.in_interface = "eth+" #sets input interface as any ethernet interface
>>> rule.src = "127.0.0.1/255.0.0.0" #the address of which packets will be rejected
>>> target = rule.create_target("DROP") #DROP target rejects the packet
>>> chain.insert_rule(rule)

#matches are optional, targets are mandatory

#By default, Python-iptables automatically performs an iptables commit after each operation. 
#i.e. after you add a rule in python-iptables, it will take effect immediately

#If, for instance, you need to traverse a chain and remove rules matching specific criteria...
#You should disable autocommits, traverse the chain, removing one or more rules, then commit it:
>>> import iptc
>>> table = iptc.Table(iptc.Table.FILTER)
>>> table.autocommit = False #Disable autocommits
>>> chain = iptc.Chain(table, "FORWARD")
>>> for rule in chain.rules:
>>>     if rule.out_interface and "eth0" in rule.out_interface:
>>>         chain.delete_rule(rule)
>>> table.commit()
>>> table.autocommit = True #re-enable them once the traversal is done
#Note that Tables are singletons, if you disable autocommit, it will be disabled for all instances of that Table

#Python-iptables supports dictionary operations!
#Rules can be converted into python dictionaries:
>>> import iptc
>>> table = iptc.Table(iptc.Table.FILTER)
>>> chain = iptc.Chain(table, "INPUT")
>>> # Create an iptc.Rule object from dictionary
>>> rule_d = {'comment': {'comment': 'Match tcp.22'}, 'protocol': 'tcp', 'target': 'ACCEPT', 'tcp': {'dport': '22'}}
>>> rule = iptc.easy.encode_iptc_rule(rule_d)
>>> # Obtain a dictionary representation from the iptc.Rule
>>> iptc.easy.decode_iptc_rule(rule)
{'tcp': {'dport': '22'}, 'protocol': 'tcp', 'comment': {'comment': 'Match tcp.22'}, 'target': 'ACCEPT'}


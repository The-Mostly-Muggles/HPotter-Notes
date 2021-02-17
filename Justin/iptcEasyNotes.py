# samples from https://github.com/ldx/python-iptables/blob/master/iptc/easy.py
# *code in this file is not necessarily intended to execute*
import iptc

#add_rule: ...add_rule(<table>, <chain>, <rule_d>, position=0, ipv6=False)
iptc.easy.add_rule('filter', 'FORWARD', "DROP")
#add a drop rule to the FORWARD chain in the filter table
#usage in Container_thread.py...
from_rule = { \
    'src': source_address, \
    'dst':dest_address, \
    'target':'ACCEPT', \
    'protocol': proto, \
    proto: {'sport': srcport, 'dport':dstport} \
}# set rule parameters, appears to establish a rule target as well
# precludes need of easy._iptc_settarget()?
iptc.easy.add_rule('filter','FORWARD',to_rule)
#calls insert_rule: ip4tc.insert_rule(rule, position=0) 

#add_chain: ...add_chain(table, chain, ipv6=False, raise_exc=True)
#""" Return True if chain was added successfully to a table, raise Exception otherwise """
#calls easy._iptc_gettable & ip4tc.create_chain
#potential usage:
#https://github.com/The-Mostly-Muggles/HPotter/blob/dev/chain.py starting at line 18:
hpotter_input_chain = filter_table.create_chain("hpotter_input")
hpotter_output_chain = filter_table.create_chain("hpotter_output")
hpotter_forward_chain = filter_table.create_chain("hpotter_forward")

hpotter_input_chain_rule = iptc.Rule()
hpotter_output_chain_rule = iptc.Rule()
hpotter_forward_chain_rule = iptc.Rule()
#iptc.easy:
hpotter_input_chain = iptc.easy.create_chain('filter', 'hpotter_input')
hpotter_output_chain = iptc.easy.create_chain('filter', 'hpotter_output')
hpotter_forward_chain = iptc.easy.create_chain('filter', 'hpotter_forward')

drop_rule = iptc.Rule()
drop_rule.target = iptc.Target(drop_rule, "DROP")

hpotter_input_chain_rule = iptc.easy.add_rule('filter','hpotter_input', drop_rule)
hpotter_output_chain_rule = iptc.easy.add_rule('filter','hpotter_output', drop_rule)
hpotter_forward_chain_rule = iptc.easy.add_rule('filter','hpotter_forward', drop_rule)
#This saves all of 2 lines of code, in chain.py... 

#potential use of delete_rule/delete_chain
iptc.easy.delete_chain('filter', hpotter_input_chain)
iptc.easey.delete_rule('filter', hpotter_input_chain, drop_rule)
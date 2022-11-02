import json
from rich import print as rprint
from genie.testbed import load
from pyats.async_ import pcall
import ipdb

def get_ospf(dev_name, testbed_value):
    ospf_neighbor = testbed_value.parse("show ip int brief")
    pretty_ospf = json.dumps(ospf_neighbor, indent=2)
    rprint(f"{dev_name}\n{pretty_ospf}\n\n")
    return ospf_neighbor


testbed = load("../testbed.yml")
testbed.connect(log_stdout = False)
result = pcall(get_ospf, dev_name=testbed.devices.keys(), testbed_value=testbed.devices.values())

ipdb.set_trace()
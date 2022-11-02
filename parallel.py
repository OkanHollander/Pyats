import json
from rich import print as rprint
from genie.testbed import load
from pyats.async_ import pcall

def get_ospf(testbed_value):
    ospf_neighbor = testbed_value.parse("show ip int brief")
    pretty_ospf = json.dumps(ospf_neighbor, indent=2)
    rprint(pretty_ospf)


testbed = load("../testbed.yml")
testbed.connect(log_stdout = False)
result = pcall(get_ospf, testbed_value=testbed.devices.values())
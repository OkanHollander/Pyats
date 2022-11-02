from genie.testbed import load
import json
from rich import print as rprint

testbed = load("../testbed.yml")

for name in testbed.devices.keys():
    dev = testbed.devices[name]
    dev.connect(log_stdout = False)
    interfaces = dev.parse("show ip int brief")
    pretty_interfaces = json.dumps(interfaces, indent=2)
    rprint(pretty_interfaces)
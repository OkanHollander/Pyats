from pyats.async_ import pcall
from genie.testbed import load
from genie.utils import Dq
from rich import print as rprint

def get_static_routes(hostname, dev):
    parsed = dev.parse("show ip route")
    get_routes = (Dq(parsed).contains('S').get_values('routes'))
    rprint(get_routes)


testbed = load("../testbed.yml")
testbed.connect(log_stdout = False)
results = pcall(get_static_routes, hostname=testbed.devices.keys(), dev=testbed.devices.values())
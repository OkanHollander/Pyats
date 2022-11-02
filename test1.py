from genie.testbed import load

testbed = load("../testbed.yml")

for name in testbed.devices.keys():
    dev = testbed.devices[name]
    dev.connect(log_stdout = False)
    interfaces = dev.parse("show ip int brief")
    print(interfaces)
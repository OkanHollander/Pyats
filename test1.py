from genie.testbed import load

testbed = load("testbed.yml")

dev = testbed.devices["CSR1000_01"]
dev.connect(log_stdout = False)

interfaces = dev.parse("show ip int brief")
print(interfaces)



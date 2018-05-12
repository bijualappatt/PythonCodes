
HostDetails=[{"Host":"192.168.0.1","Status":"ON"},{"Host":"192.168.0.2","Status":"ON"},{"Host":"192.168.0.3","Status":"OFF"},{"Host":"192.168.0.4","Status":"ON"},{"Host":"192.168.0.5","Status":"OFF"}]
print('----------All Hosts--------------------')
for host in HostDetails:
    print(host["Host"],host["Status"])

print('----------ON Hosts--------------------')
ONHosts=[host for host in HostDetails if host["Status"]=="ON"]

for host in ONHosts:
    print(host["Host"],host["Status"])


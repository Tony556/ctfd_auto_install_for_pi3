import os

with open('/etc/resolv.conf') as f:
    lists = f.read().splitlines()

for item in lists:
    item = item.split()
    if item[0] == 'nameserver':
        print item[1]

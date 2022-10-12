
input_file = open('ip.txt', 'r')

entries = 0
ip_types = {'2001:0db8':0, '2001:0e':0, 'fc/fd':0}

for line in input_file:
    if line.startswith('2001:0db8'):
        ip_types['2001:0db8']+=1
    elif line.startswith('2001:0e'):
        ip_types['2001:0e']+=1
    elif line.startswith('fc') or line.startswith('fd'):
        ip_types['fc/fd']+=1
    else:
        continue
    
    entries+=1

print('Adatsorok száma:', entries)

for k,v in ip_types.items():
    print('"'+str(k)+'" kezdetűek: '+str(v))
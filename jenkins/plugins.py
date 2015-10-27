a = open('all_plugins.txt')
b = []
for line in a:
    t = line.strip()
    if t in b:
        continue
    else:
        b.append(t)

#for t in b:
#    if t:
#        print "     wget --no-check-certificate",t," && \\"
for t in b:
    if t:
        hpi = (t.split("/"))[-1]
        print hpi.split(".")[0]

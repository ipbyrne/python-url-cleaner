# load messy paths
with open("pdfs.txt") as f:
    content = f.readlines()

content = [x.strip() for x in content] #remove white space /n
content = [x.strip('\"') for x in content] #remove quotes
content = [x.replace('vrphp1.vertexremote.net\web\CHMain-PROD', '') for x in content]
content = [x[2:] for x in content]
content = [x.replace('\\','/') for x in content]

# Add url to front
for i in range(len(content)):
    content[i] = "https://www.centralhealth.net" + content[i]


# Write output to new file
with open('output.txt', 'w') as f:
    for item in content:
        f.write("%s\n" % item)

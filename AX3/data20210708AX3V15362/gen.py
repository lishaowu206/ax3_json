#coding=utf-8
import os, time, sys, re
import simplejson as json

path = r'F:/lishaowu1221/AX3/data20210708AX3V15362/'
def GetID(f, name):
    f.seek(0,0)
    for line in f.readlines():
        if name in line:
            print(line)
            id = re.search('0x(?:[0-9a-fA-F]{2})+', line).group()
            print(id)
            return id


p = path + r'R.java'
if os.path.exists(p):
    if sys.version_info.major > 2:
        r_java_file = open(p, 'r', encoding = 'utf-8')
    else:
        r_java_file = open(p, 'r')


#create a dict which maps ts widgt name to code
p = path + r'tsidmap1221.json'
if os.path.exists(p):
    if sys.version_info.major > 2:
        json_file = open(p, 'r', encoding = 'utf-8')
    else:
        json_file = open(p, 'r')
dict = json.load(json_file)

print(dict)

for key, value in dict.items():
    name = value['name']
    print(name)

    name = name.replace('+', '')
    name = name.replace('-', '')
    id = GetID(r_java_file, name)
    value['id'] = str(id)

with open(path + r'tsidmap.json', 'w') as f:
    # json.dump(dict, f)
    json.dump(dict, f)

r_java_file.close()
json_file.close()



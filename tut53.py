import re

mystr = '''efheuheofjoehfiuf
jeiueufheohiefeifjoeheujjwwd
wdwdhwdhwuyetjwp;[evjfvdbvkjdv
kfhufhuejfojhvdbdjnkdjvdhvbd
cjwhdefeuofdcncnbvhwdjpokpoefj
joehehf;hieueyghbeyeyefeofuehfe
hfwdwuhfjnnv
jvedjoejeuhiuhfowjew
fjebfhehdvbddvndvndjvn PJ'''

# Findall, search, split, sub, finditer

patt = re.compile(r'')
matches = patt.finditer(mystr)
for match in matches:
    print(match)
    print(mystr[448:452])
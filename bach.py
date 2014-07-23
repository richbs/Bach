import re, codecs

f = codecs.open('BWV.txt', 'r', 'utf16')
uc = f.read()

BWV_RE = re.compile(r'BWV\s*[0-9]+[A-z]?', re.I)
bach_dict = {}

for b in BWV_RE.findall(uc):
    bach_dict[b] = ''

out = codecs.open('bwv_out.txt', 'w', 'utf8')

for k in bach_dict.keys():
  out.write(k + '\n')

out.close()

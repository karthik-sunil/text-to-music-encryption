from music21 import *
f = open('major-scale.mid','r')
text = f.read()
hext = unicode(text,errors='ignore')
print(hext)


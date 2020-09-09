import py_midicsv
csv_string = py_midicsv.midi_to_csv("hello_30_6.mid")
degrees  = [60, 62, 64, 65, 67, 69, 71, 72]
look_up_table = [['a','b','c','d','e','f','g','h'],['i','j','k','l','m','n','o','p'],['q','r','s','t','u','v','w','x'],['y','z','0','1','2','3','4','5'],['6','7','8','9',',','_','.',' ']]
lis = []
for i in csv_string:
    s= i.split()
    l = len(s)
    if(l>3):
        lis.append([s[1],s[l-2]])
temp = []
for i in lis:
    i[0]= (i[0].split(',')[0])
    i[1]= (i[1].split(',')[0])
    if(i[1]!='Tempo'):
        if(i[1]>='60'):
            temp.append([int(i[0]),int(i[1])])
for n in range(1, len(temp)):
    temp[n][0] = temp[n][0] - temp[n-1][0]
    print(temp[n][0])
print(temp)

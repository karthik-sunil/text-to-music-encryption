import math
from midiutil import MIDIFile
from midi2audio import FluidSynth
import py_midicsv

def main():
    key = valid_key()
    file_name = input('enter file name: ')
    target_file_name =file_name+"_c.txt"
    file_name = file_name+'.txt'
    print(file_name)
    print(target_file_name)
    f = open(file_name,'r')
    text =f.readline()
    text = text.lower()
    f.close()
    cipher = encrypt(key, text)
    f_c = open(target_file_name,'a')
    f_c.write(cipher)
    f_c.close()
    music_encrypt(text)
    print(cipher)

def valid_key():
    c = True
    x = 0
    test =True
    while(c):
        x=0
        key = input("enter the key:")
        for i in key:
            if (key.count(i)>1):
                x = x+1
                print('enter a valid key with non repeating characters')
                break
        if(x==0):
            c=False
    return key

def encrypt(key,msg): 
    cipher = ""   
    k_indx = 0
  
    msg_len = float(len(msg)) 
    msg_list = list(msg) 
    key_list = list(key)
    key_list.sort() 
    col = len(key)  
    row = int(math.ceil(msg_len / col)) 
    fill_null = int((row * col) - msg_len) 
    msg_list.extend('_' * fill_null) 
    matrix = [msg_list[i: i + col]  
              for i in range(0, len(msg_list), col)] 
   
    for _ in range(col): 
        curr_idx = key.index(key_list[k_indx]) 
        cipher += ''.join([row[curr_idx]  
                          for row in matrix]) 
        k_indx += 1
  
    return cipher 

def note_return(x):
    i = 0 
    j = 0
    look_up_table = [['a','b','c','d','e','f','g','h'],['i','j','k','l','m','n','o','p'],['q','r','s','t','u','v','w','x'],['y','z','0','1','2','3','4','5'],['6','7','8','9',',','_','.',' ']]
    for i in range(5):
         if x in look_up_table[i]:
             for j in range(8):
                 if (x == look_up_table[i][j]):
                     return [i,j]


def music_encrypt(cipher):
    degrees  = [60, 62, 64, 65, 67, 69, 71, 72]
    scale = ['C','D','E','F','G','A','B','C`']
    track    = 0
    channel  = 0
    time     = 0    # In beats
    duration = 1.00    # In beats
    tempo    = 120  # In BPM
    volume   = 120  # 0-127, as per the MIDI standard
    cipher_midi = MIDIFile(1)
    cipher_midi.addTempo(track,time,tempo)
    cipher ='hello'
    j=0
    l= []
    i = 0
    for x in cipher:
        l = note_return(x)
        cipher_midi.addNote(track, channel, degrees[l[1]], time + i, (duration/(pow(2,l[0]))), volume)
        i = i+1
    midfile = input('enter name of music file: ')
    midfile = midfile+".mid"
    with open(midfile, "wb") as output_file:
        cipher_midi.writeFile(output_file)
    fs = FluidSynth()
    output_wav = input('enter name of wav file: ')+".wav"
    fs.midi_to_audio(midfile, output_wav)        

def music_decrypt(file_name):
    csv_string = py_midicsv.midi_to_csv(file_name+".mid")
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
    
    print(temp)
    max = 0
    for n in range(len(temp)):
        temp[n][1] = degrees.index(temp[n][1])
        max = temp[n][0]
        if(temp[n][0>max]):
            max = temp[n][0] 
    for n in range(len(temp)):
        temp[n][0] = int(math.log(float(temp[n][0]/max),2))
    dec_txt = []
    for n in range(len[temp]):
        dec_txt.append(look_up_table[temp[n][0][temp[n][1]]])
    print(dec_txt)
              
main()

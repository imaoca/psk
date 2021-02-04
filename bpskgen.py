import numpy as np
import wave
import array
 
fname = 'wavgen.wav'
wf = wave.open(fname, 'w')
wf.setnchannels(1)
wf.setsampwidth(1)
wf.setframerate(8000)
 
s0 = array.array('B', [0,0,0,0,0xff,0xff,0xff,0xff]*10)
s1 = array.array('B', [0xff,0xff,0xff,0xff,0,0,0,0]*10)
dt = [1,0,0,1,0,0,1,0,1,0]*2

for i in dt:
    if i==0 :
        wf.writeframes(s0.tobytes()) 
    else:
        wf.writeframes(s1.tobytes()) 
wf.close()
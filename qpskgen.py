import numpy as np
import wave
import array
 
fname = 'qpskgen.wav'
wf = wave.open(fname, 'w')
wf.setnchannels(1)
wf.setsampwidth(1)
wf.setframerate(8000)
 
s0 = array.array('B', [0,0,0,0,0xff,0xff,0xff,0xff]*10)
s1 = array.array('B', [0,0,0xff,0xff,0xff,0xff,0,0]*10)
s2 = array.array('B', [0xff,0xff,0xff,0xff,0,0,0,0]*10)
s3 = array.array('B', [0xff,0xff,0,0,0,0,0xff,0xff]*10)
dt = [0,1,2,3,2,0,3,1]*4

for i in dt:
    if i==0 :
        wf.writeframes(s0.tobytes()) 
    if i==1 :
        wf.writeframes(s1.tobytes()) 
    if i==2 :
        wf.writeframes(s2.tobytes()) 
    if i==3 :
        wf.writeframes(s3.tobytes())     
wf.close()
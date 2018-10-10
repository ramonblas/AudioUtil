#import modules
import librosa                       #librosa module for sound analysis 
import librosa.display
from scipy.io.wavfile import write   #scipy module for writting new audio files


import numpy as np                   #module for arrays

 
import matplotlib.pyplot as plt      #module for visualization 

                          
    

def lengthPlot(file):
    x,sr = librosa.load(file)
    t = np.arange(x.size)/float(sr)
    print('File Length in seconds is: \n', (x.size)/sr ,'\nFile length in samples is: \n',x.size)
    plt.plot(t, x)
    plt.show()
def editPlotExport(archivo, desde, hasta):
    x,sr = librosa.load(archivo,sr=44100)
    y = x[desde:hasta]
    t1 = np.arange(y.size)/float(sr)
    plt.plot(t1, y)
    plt.show()
    
    new_file_name = input('Nombra el nuevo archivo: ')
    return(write(new_file_name+'.wav', sr, y))

def spectoEditPlot(file):
    x,sr = librosa.load(file)
    print('File Length in seconds is: \n', (x.size)/sr ,'\nFile length in samples is: \n',x.size)
    S = librosa.feature.melspectrogram(y=x, sr=sr, n_mels=128,fmax=8000)                                    
    plt.figure(figsize=(10,4))
    librosa.display.specshow(librosa.power_to_db(S, ref=np.max),y_axis='mel',fmax=8000,x_axis='time')        
    plt.colorbar(format='%+2.0f dB')
    plt.tight_layout()
    

    

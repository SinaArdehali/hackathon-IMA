import sounddevice as sd
from scipy.io.wavfile import write
import soundfile as sf

fs = 16000  # Sample rate
seconds = 5  # Duration of recording

myrecording = sd.rec(int(seconds * fs), samplerate=fs, channels=2)
sd.wait()  # Wait until recording is finished
write('back/output.wav', fs, myrecording)  # Save as WAV file 


# Extract audio data and sampling rate from file 
data, fs = sf.read('back/output.wav') 
# Save as FLAC file at correct sampling rate
sf.write('back/output.flac', data, fs)  
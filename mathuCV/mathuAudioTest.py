import os

import pyaudio
import wave
from pydub import AudioSegment
import socket


if __name__ == "__main__":

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((socket.gethostname(), 65000))
    s.listen(1)

    p = pyaudio.PyAudio()

    CHUNK = 1024*4
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100

    stream = p.open(format = FORMAT, channels = CHANNELS,
                    rate = RATE, input = True, output = True, frames_per_buffer = CHUNK)
    stream.start_stream()
    while stream.is_active():
        frames = []
        for i in range(0, int(RATE/CHUNK)):
            data = stream.read(CHUNK)
            frames.append(data)
            wf = wave.open("audioSample.wav", 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b"".join(frames))
            wf.close()

        sound = AudioSegment.from_file("audioSample.wav", format = "wav")
        rms = sound.rms
        print(rms)
        if rms > 1500:
            client_socket, address = s.accept()
            client_socket.sendall(bytes("succeeded", "utf-8"))
            client_socket.close()
            print("you loud")
        else:
            client_socket, address = s.accept()
            client_socket.sendall(bytes("failed", "utf-8"))
            client_socket.close()

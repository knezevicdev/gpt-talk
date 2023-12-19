import pyaudio
import keyboard
from google.cloud import speech

CHUNK = 1024


def procesuiraj():
    audio = pyaudio.PyAudio()

    stream = audio.open(format=pyaudio.paInt16, channels=1,
                        rate=16000, input=True,
                        frames_per_buffer=CHUNK)
    print("Pritisnite space da postavite pitanje. Pritisnite enter da zavrsite sa postavljanjem pitanja.")
    keyboard.wait('space')
    print("Slušam...")
    frames = []

    try:
        while True:
            data = stream.read(CHUNK)
            frames.append(data)
            if keyboard.is_pressed('enter'):
                print("Zapisujem...")
                break
    except KeyboardInterrupt:
        pass

    # zaustavi snimanje
    stream.stop_stream()
    stream.close()
    audio.terminate()

    client = speech.SpeechClient()

    audio = speech.RecognitionAudio(content=b''.join(frames))

    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="sr-RS"
    )

    response = client.recognize(config=config, audio=audio)

    # kombinuj sve rezultate u jedan string
    tekst = ""
    for result in response.results:
        tekst += result.alternatives[0].transcript + " "

    return tekst

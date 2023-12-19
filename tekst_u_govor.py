from gtts import gTTS
from pygame import mixer
import io

mixer.init()


def pricaj(tekst: str) -> None:
    audio_snimak = gTTS(text=tekst, lang="sr", slow=False)

    pseudo_file = io.BytesIO()
    audio_snimak.write_to_fp(pseudo_file)
    pseudo_file.seek(0)

    mixer.music.load(pseudo_file)
    mixer.music.play()
    while mixer.music.get_busy():
        pass

    pseudo_file.close()

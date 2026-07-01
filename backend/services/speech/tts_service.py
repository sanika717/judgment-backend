from gtts import gTTS

from config.settings import settings


class TTSService:

    @staticmethod
    def generate_audio(
        text,
        filename
    ):

        tts = gTTS(text=text)

        audio_path = (
            f"{settings.AUDIO_DIR}/{filename}.mp3"
        )

        tts.save(audio_path)

        return audio_path
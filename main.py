from Jarvis.commands import commands
from Jarvis.log import logging
from Jarvis.voice.stt import SpeechToText
from Jarvis.voice.tts import TextToSpeech

START_SCREEN = "\n" \
               "       _                  _       _             _ _             \n" \
               "      | |                (_)     (_)           | (_)            \n" \
               "      | | __ _ _ ____   ___ ___   _ ___    __ _| |___   _____   \n" \
               "  _   | |/ _` | '__\ \ / / / __| | / __|  / _` | | \ \ / / _ \  \n" \
               " | |__| | (_| | |   \ V /| \__ \ | \__ \ | (_| | | |\ V /  __/  \n" \
               "  \____/ \__,_|_|    \_/ |_|___/ |_|___/  \__,_|_|_| \_/ \___|  \n" \
               "                                                                \n" \
               "                                                                \n"


def start_listen():
    logging.info(START_SCREEN)
    stt = SpeechToText()
    tts = TextToSpeech()

    while True:
        text = stt.transcribe()

        output = commands(text)
        tts.speak(output)


if __name__ == "__main__":
    start_listen()

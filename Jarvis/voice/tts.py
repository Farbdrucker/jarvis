import json

import pyttsx3

from Jarvis.log import logging

SPEAKER_DICT = 'apple_synth_voices.json'
DEFAULT_VOICE_ID = "com.apple.speech.synthesis.voice.fiona"
DEFAULT_VOICE_RATE = 150


class _TTS:
    """
    Text To Speech helper

    I didnt fully understand it but this prevents the program of stopping right after first `engine.runAndWait()`
    cf https://www.geeksforgeeks.org/python-text-to-speech-pyttsx-module/
    """
    engine = None
    rate = None

    def onStart(self):
        logging.info('starting')

    def onWord(self, name, location, length):
        logging.info('word', name, location, length)

    def onEnd(self, name, completed):
        logging.info('finishing', name, completed)

    def __init__(self, voice_id: str, rate: int):
        self.engine = pyttsx3.init()

        self.engine.connect('started-utterance', self.onStart)
        self.engine.connect('started-word', self.onWord)
        self.engine.connect('finished-utterance', self.onEnd)

        self.engine.setProperty('voice', voice_id)
        self.engine.setProperty('rate', rate)

    def start(self, text_: str):
        """say what is written in `text_`"""
        self.engine.say(text_)
        self.engine.runAndWait()


def pardon_me():
    """speaks: `pardon me`"""
    text = 'pardon me'
    speak(text)
    logging.jarvis(text)


def can_i_help():
    """speaks: `yes? what can i do for you?`"""
    text = 'yes? what can i do for you?'
    speak(text)
    logging.jarvis(text)


def speak(msg: str):
    """speaks what is written in `msg`"""
    _speak(msg, DEFAULT_VOICE_ID, DEFAULT_VOICE_RATE)


def _speak(msg, voice_id: str, rate: int):
    """private/advanced speaking function with voice and speed rate to define"""
    tts = _TTS(voice_id, rate)
    tts.start(msg)

    # cf comment in `_TTS` somehow it prevents the program to quit after execution
    del (tts)


class TextToSpeech:
    """
    Text to speech object, wrapper for `pyttsx3` engine with human readable name initiation
    """
    def __init__(self, name: str = None, speed: int = DEFAULT_VOICE_RATE):
        self.name = name
        self.speed = speed

        if name is not None:
            with open(SPEAKER_DICT, 'r') as f:
                voices = json.load(f)

            if name not in voices.keys():
                raise NotImplementedError

            self.voice_id = voices[name]['id']

        else:
            self.voice_id = DEFAULT_VOICE_ID

    def speak(self, msg):
        """speak what is written in `msg`"""
        logging.jarvis(msg)
        _speak(msg, self.voice_id, self.speed)


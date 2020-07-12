import time

import speech_recognition as sr

from Jarvis.log import logging
from Jarvis.threads import my_threading


class SpeechToText:
    """
    Simple wrapper for SpeachRecognition Microphone and Recognizer
    """

    def __init__(self):
        self.r = sr.Recognizer()

    def transcribe(self) -> str:
        """
        listens to local microphone and recognizes speech while transcribing it
        Returns:
            predicted text as str
        """
        audio = self.listen()
        return self.recognize_text(audio)

    @my_threading
    def listen(self) -> sr.AudioData:
        """
        listens to local microphone
        Returns:
            AudioData from record
        """
        with sr.Microphone() as source:
            t0 = time.time()
            logging.info('start listening...')
            audio = self.r.listen(source)
            t1 = time.time()
            logging.info(f'stopped ... after {t1 - t0}')
        return audio

    @my_threading
    def recognize_text(self, audio: sr.AudioData) -> str:
        """
        analyzes the audio data with google API and transcribes it
        Args:
            audio: Audio Data, eg from `listen()`

        Returns:
            predited text as string
        """
        try:
            text = self.r.recognize_google(audio)
            logging.understood(text)
            return text
        except Exception as e:
            logging.warning(str(e))
            return ''

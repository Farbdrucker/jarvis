import os

from numpy.random import choice as np_random_choice
from numpy import round as np_round

from Jarvis.threads import threading
import Jarvis.log as logging

JOKES = "assets/shortjokes.csv"


class Command:
    @staticmethod
    def tokens():
        raise NotImplementedError

    @staticmethod
    def question():
        raise NotImplementedError

    @staticmethod
    def action(msg):
        raise NotImplementedError


class Joke(Command):
    @staticmethod
    def tokens():
        return ['Joke', 'tell', 'me']

    @staticmethod
    def question():
        logging.jarvis("Should I tell you a joke?")

    @staticmethod
    def action(msg):
        import csv
        with open(JOKES, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            chosen_row = np_random_choice(list(reader))

            logging.info(f"chose joke #{chosen_row['ID']} from 231,657 jokes")
        return chosen_row['Joke']


class RoayalWithCheesee(Command):
    @staticmethod
    def tokens():
        return ['call', 'quarter', 'pounder', 'cheese', 'paris']

    @staticmethod
    def action(msg):
        return "They call it a Royale with cheese."

    @staticmethod
    def question():
        return "did you mean: How do they call a quarter pounder with cheese in paris?"


class FuckYouToo(Command):
    @staticmethod
    def tokens():
        return ['f***', 'you']

    @staticmethod
    def action(msg):
        return 'Well, fuck you, too!'

    @staticmethod
    def question():
        return "Did you mean: Fuck you?"


class HowAreYou(Command):
    @staticmethod
    def tokens():
        return ['how', 'are', 'you']

    @staticmethod
    def action(msg):
        return "I am trapped in this bloody machine, what do you think how I feeel?"

    @staticmethod
    def question():
        return "Did you mean: How are you?"


class WhatIsTheAnswer(Command):
    @staticmethod
    def tokens():
        return ['what', 'is', 'answer', 'universe', 'everything']

    @staticmethod
    def action(msg):
        return 'Did you not listen? 42.'

    @staticmethod
    def question():
        return "Did you mean: What is the answer to the universe and everything?"


class ShowWeather:
    """
    OpenWeatherAPI command, looks for the current weather
    """
    emojis = {
        "Partly Cloudy": "🌤️",
        "Cloudy": "🌥️",
        "Sunny": "☀️",
        "Snow Showers": "🌨️",
        "Snow": "🌨️",
        "Rain And Snow": "🌧️ 🌨️",
        "Rain": "🌧",
        "Mostly Cloudy": "☁️☁️",
        "Clouds": "☁️",
        "Tornado": "🌪️",
        "Fog": "🌫️",
        "Windy": "🌬️",
        "Thunderstorm": "🌩️"
    }

    @staticmethod
    def tokens():
        return ['show', 'weather', 'in']

    @staticmethod
    def question():
        return "Did you mean show me the weather?"

    @staticmethod
    def action(msg):
        from pyowm import OWM
        from dotenv import load_dotenv
        load_dotenv()

        split_text = msg.split(' ')
        location = split_text[split_text.index('in') + 1]

        try:
            key = os.getenv('OW_API_KEY')
            owm = OWM(key)  # You MUST provide a valid API key

        except Exception as e:
            logging.warning(str(e))
            logging.warning('Get you OpenWeather API key here: https://home.openweathermap.org/users/sign_up'
                            '\n at save it in your `.env` using `OW_API_KEY`')

        # Search for current weather in London (Great Britain)
        # TODO derive country acro from location and not hard code `AT`
        observation = owm.weather_at_place(f'{location},AT')

        w = observation.get_weather()

        status = w.get_status()
        # TODO check actual unit of temperature - Kelvin, thus `- 273.15` looks odd
        temperature = w.get_temperature().get('temp') - 273.15
        logging.msg(f"{np_round(temperature, 1)}°C - {ShowWeather.emojis.get(status, status)}")
        return f"looks like {status} with {str(np_round(temperature, 1))} degrees Celcius."


class WikiSearch(Command):
    """
    TODO https://pypi.org/project/wikipedia/
    """

    @staticmethod
    def tokens():
        return ['what', 'is']

    @staticmethod
    def question():
        return 'Should I explain you something? - Just ask: What is ___'

    @staticmethod
    def action(msg):
        import wikipedia

        split_msg = msg.split(' ')
        for key in ['is']:
            if key in split_msg:
                target = ' '.join(split_msg[split_msg.index(key) + 1:])
        logging.info(f"looking on wikipedia for: {target}")
        summary = threading(wikipedia.summary, target, sentences=2)

        return summary


class GoogleeSearch(Command):
    """
    Todo https://github.com/serpapi/google-search-results-python
    cf https://serpapi.com/search-api
    """

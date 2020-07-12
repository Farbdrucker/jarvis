# Jarvis
my bad weather weekend project to have my personal voice assistant to tell me jokes, the current weather or read me Wikipedia articles.

## Installation
Clone the repositories
```
git clone https://github.com/Farbdrucker/jarvis.git
```

create a new conda virtual environment `conda create -n jarvis python=3.6` and install minimal `requirements.txt` with `pip -r requirements.txt`. For advanced `Command`s `advanced_requirements.txt` are required as well.



* Ensure you allow the terminal or python the access to your microphone device.

## Usage
Simply start the program by running the `main.py` file

```bash 
python3 main.py
```

Some simple interactions are predefined, for example
* **Do you know the answer to the universe and everything?**
* **How are you?**
* **How do they call a quarter pounder with cheese in Paris?**

If you want to hear some funny **jokes** download the `shortjokes.csv` from [kaggle](https://www.kaggle.com/abhinavmoudgil95/short-jokes/data) and place it into the assets and aks for
* **Tell me a joke**

If you want to browse **Wikipedia** with the voice assistant ensure to have `advanced_requirements.txt` installed and ask
* **What is KEYWORD?**

If you want the hear the current weather get you [OpenWeather API key](https://home.openweathermap.org) and save it in `.env` as `OW_API_KEY=YOUR-API-KEY` and ask for
* **Show me the weather in CITYNAME**

## TBD
* CLI with mic device selection, language and voice
* write unit tests
* integrate google search engine
* integrate spotify
* derive location and country acronym for OWM

---
GNU General Public License
# Jarvis
My bad weather weekend project to have my personal voice assistant to tell me jokes, 
the current weather or read me Wikipedia articles.

Tested locally on a Macbook Pro 2018 with Catalina, other OS could fail because of the voice synthesizer.

## Installation
Clone the repositories
```
git clone https://github.com/Farbdrucker/jarvis.git
```

create a new conda virtual environment
 
```shell
conda create -n jarvis python=3.6
```
 
and install the minimal `requirements.txt` with
 
```shell 
pip install -r requirements.txt
```

To use more advanced `Command`s, `advanced_requirements.txt` are required as well.


* Make sure that the terminal respectively python has access to the microphone

## Usage
Simply start the program by running the `main.py` file

```bash 
python3 main.py
```

Some simple interactions are predefined, for example
* **Do you know the answer to the universe and everything?**
* **How are you?**
* **How do they call a quarter pounder with cheese in Paris?**

If you want to hear some funny **jokes** download the `shortjokes.csv` from 
[kaggle](https://www.kaggle.com/abhinavmoudgil95/short-jokes/data) and place it into the assets and ask for
* **Tell me a joke**

If you want to browse **Wikipedia** with the voice assistant ensure to have `advanced_requirements.txt` installed and ask
* **What is KEYWORD?**

If you want the hear the current weather, get yourself an [OpenWeather API key](https://home.openweathermap.org) 
and save it in `.env` as `OW_API_KEY=YOUR-API-KEY` and ask for
* **Show me the weather in CITYNAME**

## TBD
* CLI with mic device, language and voice selection
* write unit tests
* integrate google search engine
* integrate spotify
* derive location and country acronym for OWM

---
GNU General Public License
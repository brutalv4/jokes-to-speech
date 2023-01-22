import pyttsx3
from requests import get

from model import Joke

INTRO = "We're about to read some jokes..."
TEN_RANDOM_JOKES = "https://official-joke-api.appspot.com/jokes/ten"


def get_jokes():
    try:
        r = get(TEN_RANDOM_JOKES)
        jokes = [Joke(joke) for joke in r.json()]
    except:
        jokes = []

    return jokes


def setup_voice_engine(engine="espeak", rate=150, volume=1, voice="en+f2"):
    try:
        engine = pyttsx3.init(engine)
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)
        engine.setProperty("voice", voice)

        print(INTRO)
        engine.say(INTRO)
        engine.runAndWait()
    except:
        engine = None

    return engine


def read_jokes(jokes, engine):
    for joke in jokes:
        print(joke)

        if engine:
            engine.say(joke)
            engine.runAndWait()


def main():
    jokes = get_jokes()
    engine = setup_voice_engine()
    read_jokes(jokes, engine)


if __name__ == "__main__":
    main()

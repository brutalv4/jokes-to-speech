import pyttsx3
from requests import get

from model import Joke

INTRO = "We're about to read some jokes..."


def setup_voice_engine(engine="espeak", rate=150, volume=1, voice="en+f2"):
    engine = pyttsx3.init(engine)
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume)
    engine.setProperty("voice", voice)

    print(INTRO)
    engine.say(INTRO)
    engine.runAndWait()

    return engine


def main():
    engine = setup_voice_engine()

    r = get("https://official-joke-api.appspot.com/jokes/ten")

    jokes = []
    for joke in r.json():
        jokes.append(Joke(joke))

    for joke in jokes:
        print(joke)
        engine.say(joke)
        engine.runAndWait()


if __name__ == "__main__":
    main()

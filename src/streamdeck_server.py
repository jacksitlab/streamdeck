#!/usr/bin/env python3

from StreamDeck.DeviceManager import DeviceManager
import time
from threading import Timer
from lib.perpetualTimer import PerpetualTimer

class StreamDeckServer:

    def __init__(self, deck, configFilename):
        self.deck = deck
        self.deck.set_key_callback(self.onKeyChanged)
        self.timer = PerpetualTimer(1, self.onTimerTick)

    def start(self):
        print("starting")
        self.deck.open()
        self.deck.reset()
        self.timer.start()

    def reset(self):
        self.deck.reset()

    def stop(self):
        print("stopping")
        self.deck.close()
        self.timer.cancel()

    def wait(self):
        while True:
            time.sleep(1)

    def onKeyChanged(self, deck, key, state):
        print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)

    def onTimerTick(self):
        print("on timer tick")


if __name__ == "__main__":
    streamdecks = DeviceManager().enumerate()

    print("Found {} Stream Deck(s).\n".format(len(streamdecks)))

    server = StreamDeckServer(streamdecks[0], 'config/config.json')

    server.start()
    server.wait()
    server.stop()

    # for index, deck in enumerate(streamdecks):
    #     deck.open()
    #     deck.reset()

    #     print_deck_info(index, deck)

    #     deck.close()

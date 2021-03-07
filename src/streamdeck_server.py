#!/usr/bin/env python3

import os
import time
import re
import cairosvg
import io
from threading import Timer
from PIL import Image, ImageDraw, ImageFont
from StreamDeck.DeviceManager import DeviceManager
from StreamDeck.ImageHelpers import PILHelper
from lib.perpetualTimer import PerpetualTimer
from lib.config import StreamDeckConfig
from lib.imageCache import ImageCache
from lib.denonClient import DenonClient
from lib.foobarClient import FoobarClient
from lib.kodiClient import KodiClient
from lib.executionResolver import ExecutionResolver
from lib.execution.denonExecuter import DenonExecuter
from lib.execution.foobarExecuter import FoobarExecuter
from lib.execution.kodiExecuter import KodiExecuter

class StreamDeckServer:

    def __init__(self, deck, configFilename):
        self.deck = deck
        self.config = StreamDeckConfig(configFilename)
        self.deck.set_key_callback(self.onKeyChanged)
        self.timer = None
        #self.timer = PerpetualTimer(1, self.onTimerTick)
        self.imageCache = ImageCache('.cache', True)
        self.executor = ExecutionResolver(self.config)

    def start(self):
        print("starting")
        self.deck.open()
        self.deck.reset()
        self.initKeys()
        if self.timer:
            self.timer.start()

    def reset(self):
        self.deck.reset()

    def stop(self):
        print("stopping")
        self.deck.close()
        if self.timer:
            self.timer.cancel()

    def wait(self):
        while True:
            time.sleep(1)

    def initKeys(self):
        for key in range(self.deck.key_count()):
            self.updateKeyImage(key, False)

    def updateKeyImage(self, key, state):
        # Determine what icon and label to use on the generated key.
        #key_style = get_key_style(deck, key, state)

        # Generate the custom key with the requested image and label.
        image = self.renderKeyImage(self.config.getItemConfig(key))

        # Use a scoped-with on the deck to ensure we're the only thread using it
        # right now.
        with self.deck:
        # Update requested key with the generated image.
            self.deck.set_key_image(key, image)

    def renderKeyImage(self, config):

        if (config is None) or (config.image is None) or (len(config.image)==0):
            icon = Image.new('RGB', (72, 72))
        else:
            print("render image "+config.image)
            try:
                icon = self.imageCache.get(config.image)
            except Exception as e:
                print("problem loading image from cache "+config.image+":"+e)
                icon = Image.new('RGB', (72, 72))
        margin = self.config.defaultMargin
        image = PILHelper.create_scaled_image(self.deck, icon, margins=[margin, margin, margin, margin])

        # Load a custom TrueType font and use it to overlay the key index, draw key
        # label onto the image a few pixels from the bottom of the key.
        #draw = ImageDraw.Draw(image)
        #font = ImageFont.truetype(font_filename, 14)
        #draw.text((image.width / 2, image.height - 5), text=label_text, font=font, anchor="ms", fill="white")

        return PILHelper.to_native_format(self.deck, image)

    def onKeyChanged(self, deck, key, state):
        print("Deck {} Key {} = {}".format(deck.id(), key, state), flush=True)
        if not state:
            return
        keyConfig = self.config.getItemConfig(key)
        if not keyConfig is None:
            if len(keyConfig.executions) > 0:
                self.resolveExecutions(keyConfig.executions)
            else:
                print("nothing to exec")

    def onTimerTick(self):
        print("on timer tick")

    def resolveExecutions(self, execs):
        for execution in execs:
            self.executor.execute(execution)

    def resolveExecutionExternal(self, execution):
        print("execute external command "+ execution)
        pass


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

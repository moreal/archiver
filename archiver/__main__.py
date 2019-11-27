import discord
import os
import sys
import logging

logger = logging.getLogger('logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

API_KEY = os.environ['ARCHIVER_API_KEY']


class Archiver(discord.Client):
    def dispatch(self, event: str, *args, **kwargs):
        super().dispatch(event, *args, **kwargs)
        if not event.startswith('socket'):
            logger.debug(event)
            logger.debug(args)
            logger.debug(kwargs)

client = Archiver()
client.run(API_KEY)

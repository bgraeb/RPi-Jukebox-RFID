#! /usr/bin/python
from mpd import MPDClient

client = MPDClient()
client.timeout = 10000
client.idletimeout = None
client.connect("localhost", 6600)
client.pause()
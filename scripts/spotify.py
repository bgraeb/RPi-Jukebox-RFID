#! /usr/bin/python
import sys
from mpd import MPDClient

playlist = sys.argv[1]

client = MPDClient()
client.timeout = 10000
client.idletimeout = None
client.connect("localhost", 6600)
client.clear()
client.add(playlist)
client.play()
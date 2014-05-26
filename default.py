#!/usr/bin/python
# -*- coding: utf-8 -*-

#  Copyright (C) 2014 KodeKarnage
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with XBMC; see the file COPYING.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#


import xbmcgui
import xbmc
import xbmcaddon
import sys
import os
import json

clear_playlist   = {"jsonrpc": "2.0","id": 1, "method": "Playlist.Clear",			"params": {"playlistid": 1}}
get_movies       = {"jsonrpc": "2.0",'id': 1, "method": "VideoLibrary.GetMovies", 	"params": { "filter": {"field": "playcount", "operator": "is", "value": "0"}, "properties" : ["playcount", "title", "file"] }}
get_moviesa      = {"jsonrpc": "2.0",'id': 1, "method": "VideoLibrary.GetMovies", 	"params": { "properties" : ["playcount", "title"] }}

__addon__        = xbmcaddon.Addon()
__addonid__      = __addon__.getAddonInfo('id')
__addonversion__ = tuple([int(x) for x in __addon__.getAddonInfo('version').split('.')])
__setting__      = __addon__.getSetting
lang             = __addon__.getLocalizedString
dialog           = xbmcgui.Dialog()
scriptPath       = __addon__.getAddonInfo('path')
scriptName       = __addon__.getAddonInfo('Name')

WINDOW           = xbmcgui.Window(10000)

__resource__     =  os.path.join(scriptPath, 'resources')
sys.path.append(__resource__)



def log(message, label = '', reset = False):
	if keep_logs:
		logmsg       = '%s : %s :: %s ' % (__addonid__, label, message)
		xbmc.log(msg = logmsg)


log('language = ' + str(language))


def gracefail(message):
	dialog.ok("JFChooseSomething",message)
	sys.exit()


def json_query(query, ret):
	try:
		xbmc_request = json.dumps(query)
		result = xbmc.executeJSONRPC(xbmc_request)
		#print result
		#result = unicode(result, 'utf-8', errors='ignore')
		#log('result = ' + str(result))
		if ret:
			return json.loads(result)['result']
		else:
			return json.loads(result)
	except:
		return {}


if __name__ == "__main__":
	pass



'''
We suffer from too much choice.

JF Choose Something is the addon that forces the decision.

The wife is always saying, "lets watch a movie", and you say, "Sure, whatever you want to watch honey"

She then spends 5 minutes cycling through all the movies in your library before saying, "I dont know, what do you want to watch?"

jfchoosesomething just grabs 4 unwatched movies at random and says, PICK ONE OF THESE!

You can mark a movie as watched, or as ignored, so that it doesnt show in the future.

There is no backing out of the choice. If you dont select one of the movies, a completely random one will be chosen for you.

You have 30 seconds to make a decision. An overlay counts down.

The movie details show on the screen. (Use playlist view?)


'''
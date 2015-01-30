# coding=utf-8
from __future__ import absolute_import

import flask
import octoprint.plugin
import logging
import time


##~~ Init Plugin and Metadata

##__plugin_name__ = "OnScreenKeyboard"
##__plugin_version__ = "0.1"
##__plugin_author__ = "Pim Rutgers"
##__plugin_url__ = ""
##__plugin_description__ = "Adds on screen keyboard to OctoPrint"

def __plugin_init__():
		global _plugin
		global __plugin_implementations__

		_plugin = OnScreenKeyboard()
		__plugin_implementations__ = [_plugin]

class OnScreenKeyboard(octoprint.plugin.TemplatePlugin,
						  octoprint.plugin.AssetPlugin):

		##~~ TemplatePlugin
		# this might needs some vars later on

		##~~ AssetsPlugin
		def get_assets(self):
			return dict(
				js=["js/onscreenkeyboard.js",
					"js/jquery.keyboard.js",
					"js/jquery.ui.position.js"],
				css=["css/onscreenkeyboard.css"]
			)

"""Config flow for mikromarz integration."""
from __future__ import annotations

import logging
import json
import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN
from .Config import Config

_LOGGER = logging.getLogger(__name__)

class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
	"""Config flow."""
	VERSION = 1

	async def async_step_user(self, input: dict|None = None):
		_LOGGER.info(input)
		if input is not None:
			for key, value in input.items():
				Config.set(key, value)

		data_schema = {
			vol.Required("url", description="Host of the Mikromarz device."): str
		}

		return self.async_show_form(
			step_id="user",
			data_schema=vol.Schema(data_schema)
		)
		



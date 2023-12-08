"""Config flow for mikromarz integration."""
from __future__ import annotations

import logging
import voluptuous as vol

from homeassistant import config_entries

from .const import DOMAIN
from .Config import Config
from .Validator import Validator


class ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
	"""Config flow."""
	VERSION = 1
	_LOGGER = logging.getLogger(__name__)

	def __init__(self) -> None:
		self.config = Config()
		self.validator = Validator()



	async def async_step_user(self, input: dict|None = None):
		if input is not None:
			# for key, value in input.items():
			# 	self.config.set(key, value)
			valid = await self.validator.isValidIP(input["host"])
			if valid:
				return self.async_create_entry(
					title="Wattmeter host",
					data={
						"host": input["host"]
					},
				)

		data_schema = {
			vol.Required("host", description="Host of the Mikromarz device."): str
		}

		return self.async_show_form(
			step_id="user",
			data_schema=vol.Schema(data_schema)
		)



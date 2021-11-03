"""
VideoPlayerBot, Telegram Video Chat Bot
Copyright (c) 2021  Asm Safone <https://github.com/AsmSafone>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>
"""

import os
from os import getenv
from dotenv import load_dotenv

load_dotenv()

admins = {}
OLD_PMS = {}
AUDIO_CALL = {}
VIDEO_CALL = {}
API_ID = int(getenv("API_ID", "6847114"))
API_HASH = getenv("API_HASH", "7f2c9b9ac20e6840d13f9ca85e1c4e2d")
BOT_TOKEN = getenv("BOT_TOKEN", "2072190749:AAHz8P1_ADtIp4n9p4UdRvS1pyGxldjnD4Q")
SESSION_STRING = getenv("SESSION_STRING", "BQAWkilQyDXW0RDJxY4SUVRwWdTUi3VDQtsmLQhadyJuOg1VhfJINsDs-VNvQuPJbGKOEyRqJL0G7haGXazAwXOo59l6UNJGiVanBpviu_HcNJI7f39JODggZ-pumT8RUbEh28fAYnii_2ekwWa0kOGOS7oq3_ySAJb5hwDp2RnXF1JjMfauy-NF3ut8ralAli-F7laO0Hc7fi0m4ggerhAfDnDPwK8hq50fwma25T8lT9W32ykey8SWpncn-huWTGETzfik22mhcAdXZ9xS6oJufdYUXHR8Fx6BydcsLarq5BzKDZ5LPH_zskq4YK1dScg1v9CXIWMxBDHS-wSZs67aaT9o4gA")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "anonmusikid")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "AsmSafone")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "alexaassisten")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "927625147").split()))
REPLY_MESSAGE = getenv("REPLY_MESSAGE", "Dont PM this account or your grup will be ban forever!")
if not REPLY_MESSAGE:
    REPLY_MESSAGE = None
else:
    REPLY_MESSAGE = REPLY_MESSAGE

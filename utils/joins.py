"""
The IdleRPG Discord Bot
Copyright (C) 2018-2021 Diniboy and Gelbpunkt
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU Affero General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Affero General Public License for more details.
You should have received a copy of the GNU Affero General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""
from discord.interactions import Interaction
from discord.ui import Button, View
from discord.user import User

from utils.i18n import _


class JoinView(View):
    def __init__(self, join_button: Button, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        join_button.callback = self.button_pressed
        self.add_item(join_button)
        self.joined: set[User] = set()

    async def button_pressed(self, interaction: Interaction) -> None:
        self.joined.add(interaction.user)
        await interaction.response.send_message(
            _("You have joined the raid."), ephemeral=True
        )

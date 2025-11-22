#  Pyrogram - Telegram MTProto API Client Library for Python
#  Copyright (C) 2017-present Dan <https://github.com/delivrance>
#
#  This file is part of Pyrogram.
#
#  Pyrogram is free software: you can redistribute it and/or modify
#  it under the terms of the GNU Lesser General Public License as published
#  by the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  Pyrogram is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU Lesser General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License
#  along with Pyrogram.  If not, see <http://www.gnu.org/licenses/>.

from pyrogram import types
from ..object import Object

from typing import List, Optional


class InputPollOption(Object):
    """Describes a poll option to create.

    Parameters:
        text (``str``):
            Option text, 1–100 characters.

        entities (List of :obj:`~pyrogram.types.MessageEntity`, optional):
            List of special entities that appear in the option text.

            The server only accepts :obj:`~pyrogram.enums.MessageEntityType.CUSTOM_EMOJI` entities.
            Other entity types (such as bold or italic) are silently ignored by the server:
            they do not cause an error, but they are not rendered.
    """

    def __init__(
        self,
        text: str,
        entities: Optional[List["types.MessageEntity"]] = None,
    ):
        super().__init__()

        self.text = text
        self.entities = entities
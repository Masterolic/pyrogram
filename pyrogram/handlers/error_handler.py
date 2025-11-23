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

from collections.abc import Sequence
from typing import Callable

from .handler import Handler


class ErrorHandler(Handler):
    """The Error handler class. Used to handle unexpected errors.

    It is intended to be used with :meth:`~pyrogram.Client.add_handler`.

    For a more convenient way to register this handler, see the
    :meth:`~pyrogram.Client.on_error` decorator.

    Parameters:
        callback (``Callable``):
            A function that will be called whenever an unexpected error is raised.
            It takes the following positional arguments: *(exception, handler, client, *args)*.

        exceptions (``Exception`` | ``Sequence[Exception]``, *optional*):
            An exception type or a sequence of exception types that this handler should handle.
            If None, the handler will catch any exception that is a subclass of ``Exception``.
            Defaults to ``None``.

    Other parameters passed to the callback:
        exception (``Exception``):
            The Exception instance that was raised.

        handler (:obj:`~pyrogram.handlers.handler.Handler`):
            The Handler instance from which the exception was raised.

        client (:obj:`~pyrogram.Client`):
            The Client instance, useful when calling other API methods inside the error handler.

        *args (``tuple[Any, ...]``):
            The original arguments passed to the handler.
    """

    def __init__(self, callback: Callable, exceptions: Exception | Sequence[Exception, ...] | None = None):
        super().__init__(callback)

        exceptions = exceptions or (Exception,)
        if not isinstance(exceptions, tuple):
            exceptions = tuple(exceptions) if isinstance(exceptions, Sequence) else (exceptions,)

        self.exceptions = exceptions
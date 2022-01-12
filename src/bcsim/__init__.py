
"""
.. include:: ../../docs/intro.md
"""

__version__ = '1.0.4'

from .clocks import Clock  # noqa
from .clocks import FastClock  # noqa
from .rail import Ball  # noqa
from .rail import Rail  # noqa
from .tools import clear  # noqa
from .tools import runSimulation  # noqa

__pdoc__ = {}
__pdoc__['clocks.Clock.__str__'] = True
__pdoc__['rail.Rail.__eq__'] = True

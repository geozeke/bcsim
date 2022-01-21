
"""
.. include:: ../../docs/intro.md
"""

__version__ = '1.0.5'

# Need to enforce the correct dependency ordering, with the rail class coming
# first. This avoids circular references when isort starts rearranging things.

from .rail import Ball  # isort: skip
from .rail import Rail  # isort: skip
from .clocks import Clock
from .clocks import FastClock
from .tools import clear
from .tools import runSimulation

__pdoc__ = {}
__pdoc__['clocks.Clock.__str__'] = True
__pdoc__['rail.Rail.__eq__'] = True
__pdoc__['__main__'] = True

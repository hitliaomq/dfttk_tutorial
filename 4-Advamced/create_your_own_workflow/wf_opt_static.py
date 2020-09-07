#!python
#A work flow run OptimizeFW followed by StaticFW
#

from dfttk.fworks import OptimizeFW, StaticFW
from fireworks import Workflow, LaunchPad
from pymatgen import Structure
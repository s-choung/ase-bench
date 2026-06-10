from ase import Atoms
from ase.build import bulk
from ase.md import VelocityVerlet, NVTBerendsen
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT
from ase import units
import numpy as np

ag = bulk('Ag', 'fcc', cubic=True).repeat(2)
ag.calc = EMT()

dyn = NVTBerendsen(ag, timestep=5*units.fs, temperature_K=500, taut=0.1*1000*units.fs, trajectory=None)

def print_temp():
    if dyn.nsteps % 50 == 0:
        print(f"Step {dyn.nsteps}: Temperature = {ag.get_temperature():.2f} K")

dyn.attach(print_temp, interval=1)
dyn.run(200)

from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase import units
import numpy as np

atoms = bulk('Al', 'fcc', a=4.0)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = 'EMT'

# Pressure conversion: 1 GPa = 10 eV/Ang^3
pressure = 10 * units.GPa  # 10 GPa

# NPT simulation parameters
npt = NPTBerendsen(atoms, timestep=10 * units.fs,
                    temperature=500 * units.K,
                    pressure=pressure,
                    logfile='npt.log')

print("Initial cell volume:", atoms.get_cell_volume())

npt.run(100)  # Run for 100 steps

print("Final cell volume:", atoms.get_cell_volume())

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.6)
atoms = atoms.repeat((3, 3, 3))
atoms.calc = EMT()

npt = NPTBerendsen(atoms, timestep=5 * units.fs,
                   temperature=300 * units.kB,
                   pressure=1.0 * units.bar,
                   t_tau=100 * units.fs,
                   p_tau=1000 * units.fs)

print("Initial cell volume:", atoms.get_cell_volume())
print("Initial pressure:", atoms.get_stress()[1, 1])

npt.run(nsteps=200)

print("Final cell volume:", atoms.get_cell_volume())
print("Final pressure:", atoms.get_stress()[1, 1])

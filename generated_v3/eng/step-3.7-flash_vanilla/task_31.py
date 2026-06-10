from ase.build import fcc
from ase.calculators.emt import EMT
from ase.md.npt import NPTBerendsen
from ase.units import GPa, fs

atoms = fcc('Al', size=(2, 2, 2))
atoms.set_calculator(EMT())

print(f"Initial volume: {atoms.get_volume():.2f} Å³")

dyn = NPTBerendsen(atoms, timestep=1 * fs, temperature=500, pressure=10 * GPa)
dyn.run(100)

print(f"Final volume: {atoms.get_volume():.2f} Å³")

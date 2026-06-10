from ase.build import fcc
from ase.md.npt import NPTBerendsen
from ase.calculators.emt import EMT
from ase.units import Bohr, fs, bar

atoms = fcc('Cu', size=3)
calc = EMT()
atoms.calc = calc

npt = NPTBerendsen(atoms, 300 * units.kB, 1 * units.bar, timestep=5 * fs, taut=100 * units.fs, taup=1000 * units.fs)

print("Initial cell volume:", atoms.get_cell_volume())
print("Initial pressure:", atoms.get_potential_energy())

npt.run(200)

print("Final cell volume:", atoms.get_cell_volume())
print("Final pressure:", atoms.get_potential_energy())

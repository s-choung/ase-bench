from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Before optimization:\nCell volume: {atoms.get_volume():.3f} | Energy: {atoms.get_potential_energy():.3f}")

filtered = FrechetCellFilter(atoms)
BFGS(filtered, fmax=0.01).run()

print(f"After optimization:\nCell volume: {atoms.get_volume():.3f} | Energy: {atoms.get_potential_energy():.3f}")

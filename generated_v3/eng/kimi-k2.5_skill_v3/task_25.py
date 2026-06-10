from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Initial cell: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")

BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

print(f"Final cell: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Final energy: {atoms.get_potential_energy():.4f} eV")

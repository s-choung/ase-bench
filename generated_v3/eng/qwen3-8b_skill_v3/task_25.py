from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

print("Initial cell size:", atoms.get_cell_lengths_and_angles()[0])
print("Initial energy:", atoms.get_potential_energy())

filtered = FrechetCellFilter(atoms)
opt = BFGS(filtered)
opt.run(fmax=0.01)

print("Final cell size:", atoms.get_cell_lengths_and_angles()[0])
print("Final energy:", atoms.get_potential_energy())

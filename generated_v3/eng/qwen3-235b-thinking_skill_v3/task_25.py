from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.5)
initial_cell = atoms.get_cell_lengths_and_angles()
initial_energy = atoms.get_potential_energy()

atoms.calc = EMT()
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

final_cell = atoms.get_cell_lengths_and_angles()
final_energy = atoms.get_potential_energy()

print(f"Initial cell: {initial_cell}, energy: {initial_energy:.6f} eV")
print(f"Final cell: {final_cell}, energy: {final_energy:.6f} eV")

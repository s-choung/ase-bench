from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Initial lattice constant: {atoms.cell[0, 0]:.4f} Å")
print(f"Initial energy: {atoms.get_potential_energy():.4f} eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"Optimized lattice constant: {atoms.cell[0, 0]:.4f} Å")
print(f"Optimized energy: {atoms.get_potential_energy():.4f} eV")

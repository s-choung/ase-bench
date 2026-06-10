from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print("Before:")
print(f"Cell: {atoms.cell.cellpar()}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("\nAfter:")
print(f"Cell: {atoms.cell.cellpar()}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")

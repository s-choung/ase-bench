from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

print("Before optimization:")
print(f"Cell: {atoms.cell.lengths()[:3]}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")

opt = BFGS(FrechetCellFilter(atoms), trajectory='opt.traj')
opt.run(fmax=0.01)

print("\nAfter optimization:")
print(f"Cell: {atoms.cell.lengths()[:3]}")
print(f"Energy: {atoms.get_potential_energy():.4f} eV")

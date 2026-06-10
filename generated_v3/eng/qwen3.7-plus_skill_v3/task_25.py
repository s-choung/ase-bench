from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

print("Before optimization:")
print(f"Cell:\n{atoms.get_cell()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print("After optimization:")
print(f"Cell:\n{atoms.get_cell()}")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")

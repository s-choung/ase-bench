from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Initial cell:\n{atoms.get_cell()}")
print(f"Initial energy: {atoms.get_potential_energy():.6f} eV")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"Final cell:\n{atoms.get_cell()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")

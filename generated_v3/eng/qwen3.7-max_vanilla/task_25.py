from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

atoms = bulk('Cu', 'fcc', a=3.5, cubic=True)
atoms.rattle(0.02)
atoms.calc = EMT()

print(f"Initial Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Initial Cell:\n{atoms.cell[:]}")

opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

print(f"\nFinal Energy: {atoms.get_potential_energy():.4f} eV")
print(f"Final Cell:\n{atoms.cell[:]}")

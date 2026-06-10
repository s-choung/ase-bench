from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import FrechetCellFilter
from ase.optimize import BFGS

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

e0 = atoms.get_potential_energy()
print("Before optimization:")
print("Cell:\n", atoms.cell)
print("Energy:", e0)

cf = FrechetCellFilter(atoms)
opt = BFGS(cf)
opt.run(fmax=0.01)

e1 = atoms.get_potential_energy()
print("\nAfter optimization:")
print("Cell:\n", atoms.cell)
print("Energy:", e1)

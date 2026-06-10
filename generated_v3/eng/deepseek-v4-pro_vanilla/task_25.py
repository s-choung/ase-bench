from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize import BFGS

# Initial Cu FCC structure
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

# Before optimization
a0 = atoms.cell[0, 0]
e0 = atoms.get_potential_energy()
print(f"Before optimization: a = {a0:.3f} Å, energy = {e0:.3f} eV")

# Setup filter and optimizer
filter = FrechetCellFilter(atoms)
opt = BFGS(filter)
opt.run(fmax=0.01)

# After optimization
a1 = atoms.cell[0, 0]
e1 = atoms.get_potential_energy()
print(f"After optimization: a = {a1:.3f} Å, energy = {e1:.3f} eV")

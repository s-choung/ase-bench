from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create initial FCC Cu structure
atoms = bulk('Cu', fcc=True, a=3.6)

# Attach calculator
atoms.calc = EMT()

# Print initial properties
print(f"Initial cell:\n{atoms.cell}\nInitial energy: {atoms.get_energy():.4f} eV\n")

# Set up cell filter and optimizer
ecf = FrechetCellFilter(atoms)
opt = BFGS(ecf, logfile=None)

# Optimize until fmax < 0.01 eV/Å
opt.run(fmax=0.01)

# Print final properties
print(f"Final cell:\n{atoms.cell}\nFinal energy: {atoms.get_energy():.4f} eV")

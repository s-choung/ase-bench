from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create Cu FCC bulk with initial guess
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

print(f"Before: cell size={atoms.cell.lengths().tolist()}, energy={atoms.get_potential_energy():.4f} eV")

# Simultaneously optimize lattice and positions
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)

print(f"After:  cell size={atoms.cell.lengths().tolist()}, energy={atoms.get_potential_energy():.4f} eV")

from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.cellfilter import FrechetCellFilter
from ase.constraints import FixAtoms
import numpy as np

# Initialize Cu FCC bulk structure
a0 = 3.615  # Lattice constant for Cu in Angstroms
Cu = Atoms('Cu', positions=[(0, 0, 0)], latticeconstant=a0)
Cu.set_repeat((3, 3, 3))  # 3x3x3 supercell for a bulk-like system

# Use EMT as the calculator
Cu.calc = EMT()

# Apply FrechetCellFilter to allow optimization of cell shape and size
Cu = FrechetCellFilter(Cu)

# Fix atomic positions initially (optional, to focus on lattice optimization)
Cu.constraints = FixAtoms(mask=[True]*len(Cu))

# BFGS optimizer
optimizer = BFGS(Cu, trajectory='Cu_opt.traj', maxforcetol=0.01)

# Run optimization
optimizer.run(fmax=0.01)

# Print cell size and energy before and after optimization
print("Initial cell parameters:")
print(f"a0 = {a0} Å")
print(f"Initial energy: {Cu.get_potential_energy():.4f} eV")

print("\nOptimized cell parameters:")
print(f"Optimized lattice constant: {np.linalg.norm(Cu.cell).round(4)} Å")
print(f"Optimized energy: {Cu.get_potential_energy():.4f} eV")

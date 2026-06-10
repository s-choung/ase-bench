from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Initial setup
atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

# Print initial values
print(f"Initial cell size: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Initial energy: {atoms.get_potential_energy():.5f} eV")

# Optimization
opt = BFGS(FrechetCellFilter(atoms), trajectory='cu_opt.traj')
opt.run(fmax=0.01)

# Print final values
print(f"Final cell size: {atoms.get_cell_lengths_and_angles()[:3]}")
print(f"Final energy: {atoms.get_potential_energy():.5f} eV")

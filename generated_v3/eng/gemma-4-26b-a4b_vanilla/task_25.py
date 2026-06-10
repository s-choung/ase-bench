from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.constraints import ExpCellFilter
from ase.optimize import BFGS

# Initialize Cu FCC bulk (using EMT for demonstration as requested)
# Note: EMT is for metals, but intended for Cu here for script logic
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

print(f"Before optimization:")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell: {atoms.get_cell().get_volume():.4f} Å³")

# Apply Filter for simultaneous cell and position optimization
ecf = ExpCellFilter(atoms)

# Optimize
opt = BFGS(ecf, logfile=None)
opt.run(fmax=0.01)

print(f"\nAfter optimization:")
print(f"Energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell: {atoms.get_cell().get_volume():.4f} Å³")
print(f"Lattice constant: {atoms.get_cell().lengths()[0]:.4f} Å")

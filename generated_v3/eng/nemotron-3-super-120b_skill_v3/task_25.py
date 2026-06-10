from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.6)   # initial guess for lattice constant
atoms.calc = EMT()

# Get and print initial cell and energy
initial_cell = atoms.get_cell_lengths_and_angles()
initial_energy = atoms.get_potential_energy()
print(f"Initial cell (a,b,c,α,β,γ): {initial_cell}")
print(f"Initial energy: {initial_energy:.6f} eV")

# Optimize cell + positions using FrechetCellFilter + BFGS
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Get and print final cell and energy
final_cell = atoms.get_cell_lengths_and_angles()
final_energy = atoms.get_potential_energy()
print(f"Optimized cell (a,b,c,α,β,γ): {final_cell}")
print(f"Optimized energy: {final_energy:.6f} eV")

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize.precon import PreconLBFGS
from ase.filters import FrechetCellFilter

# Build Ni FCC bulk
atoms = bulk('Ni', 'fcc')
# Set EMT calculator
atoms.calc = EMT()
# Initialize PreconLBFGS with cell filter and auto preconditioner
opt = PreconLBFGS(FrechetCellFilter(atoms), precon='auto')
# Run optimization to fmax=0.01
opt.run(fmax=0.01)

# Print required results
print(f"Steps: {opt.get_number_of_steps()}")
print(f"Final energy: {atoms.get_potential_energy():.6f} eV")
print(f"Cell parameters (a,b,c,α,β,γ): {atoms.get_cell_lengths_and_angles()}")

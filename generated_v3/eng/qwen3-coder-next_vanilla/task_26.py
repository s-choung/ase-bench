from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import PreconLBFGS
from ase.lattice.cubic import FaceCenteredCubic

# Create Ni FCC bulk
ni = FaceCenteredCubic('Ni', size=(1, 1, 1), pbc=True)
ni.set_calculator(EMT())

# Optimize using PreconLBFGS with auto preconditioner
opt = PreconLBFGS(ni, precon='auto')
opt.run(fmax=0.01)

# Print results
print(f"Number of steps: {opt.get_number_of_steps()}")
print(f"Final energy: {ni.get_total_energy():.6f} eV")
print("Cell parameters (Angstrom):")
print(ni.get_cell_lengths_and_angles())

from ase import Atoms
from ase.md.verlet import VelocityVerlet
from ase.calculators import EMT, LJ
import numpy as np

# Create Cu FCC bulk
atoms = Atoms.from_miller_indices([(1,0,0), (1,1,0), (1,2,0), (1,1,1), (1,2,1), (1,2,2)])
atoms.cell = np.eye(3)
atoms.vacuum = 1.0

# Set calculator and parameters
calc = EMT(lwave="SE",  # Use SE interpolator, more accurate
          ecut=4.0,  # Cutoff energy
          kpts=4) # k-point grid size
atoms.set_calculator(calc)

# Add LJ potential
atoms.set_lj_parameters(r_min=2.0, r_max=8.0, epsilon=0.2, sigma=1.0)
calc = LJ(epsilon=0.2, sigma=1.0) # Re-assign LJ calculator
atoms.set_calculator(calc)


# MD setup
md = VelocityVerlet(atoms, box_style='cubic')
md.pscale = 2.87 # Angstroms

# Initial temperature
temp = 300.0

# NVE MD simulation
for step in range(50):
    md.md(step_filename="cu_nve.xyz") # Optional output
    energy = atoms.get_potential_energy()
    print(f"Step {step+1}: Energy = {energy}")

# Print initial and final energy
print(f"Initial total energy: {atoms.get_potential_energy()}")
print(f"Final total energy: {atoms.get_potential_energy()}")

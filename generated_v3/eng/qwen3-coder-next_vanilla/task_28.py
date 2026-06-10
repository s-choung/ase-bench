import numpy as np
from ase import Atoms
from ase.lattice.cubic import FaceCenteredCubic
from ase.units import kB
from ase.md.langevin import Langevin
from ase.calculators.emt import EMT

# Create Cu FCC 2x2x2 supercell
atoms = FaceCenteredCubic('Cu', size=(2, 2, 2))

# Set EMT calculator
atoms.set_calculator(EMT())

# Set initial temperature to 300 K
temperature = 300.0
timestep = 5.0  # fs
steps = 200
dt = timestep  # fs

# Create Langevin dynamics
dyn = Langevin(atoms, timestep * units.fs, temperature * kB, 0.02)

# Function to get current temperature from kinetic energy
def get_temperature(atoms):
    kinetic_energy = atoms.get_kinetic_energy()
    # For N atoms, degrees of freedom = 3N
    dof = 3 * len(atoms)
    # <E_kin> = (dof/2) * kB * T => T = 2*E_kin / (dof * kB)
    return 2 * kinetic_energy / (dof * kB)

# Run MD with temperature ramp
for step in range(steps):
    # Linear temperature ramp: 300 K to 600 K over 200 steps
    current_temp = 300.0 + (600.0 - 300.0) * step / (steps - 1)
    dyn.set_temperature(current_temp * kB)
    
    # Take one MD step
    dyn.run(1)
    
    # Print temperature every 50 steps
    if (step + 1) % 50 == 0 or step == 0:
        temp = get_temperature(atoms)
        print(f"Step {step + 1}: Temperature = {temp:.1f} K")

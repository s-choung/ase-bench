import numpy as np
from ase import units
from ase.build import bulk
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.optimize import BFGS
from ase.calculators.emt import EMT

# Setup Pd supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initial relaxation (to ensure stable starting point)
BFGS(atoms).run(fmax=0.05)

# Initialize velocities for NVE
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Energy tracking function
def get_total_energy(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

e_start = get_total_energy(atoms)

# MD setup
steps = 200
timestep = 2 * units.fs
dyn = VelocityVerlet(atoms, timestep=timestep)

# Run MD
dyn.run(steps)

e_end = get_total_energy(atoms)

print(f"Initial Total Energy: {e_start:.6f} eV")
print(f"Final Total Energy:   {e_end:.6f} eV")
print(f"Energy Difference:    {abs(e_end - e_start):.6f} eV")

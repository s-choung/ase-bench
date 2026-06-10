from ase import Atoms
from ase.calculators.emt import EMT
from ase.io import Trajectory
from ase.md.langevin import Langevin
from ase import units
import numpy as np

# Create Cu FCC bulk 2x2x2 supercell
cu_bulk = Atoms('Cu', positions=[[0,0,0]], cell=[3.6, 3.6, 3.6], pbc=True)
cu_supercell = cu_bulk * (2, 2, 2)

# Set calculator
cu_supercell.calc = EMT()

# Initialize velocities for 300K
cu_supercell.get_kinetic_energy()
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
MaxwellBoltzmannDistribution(cu_supercell, temperature_K=300)

# Get initial temperature and energy
init_temp = cu_supercell.get_temperature()
init_energy = cu_supercell.get_potential_energy()

# Set up Langevin MD
dyn = Langevin(cu_supercell, 5 * units.fs, temperature_K=300, friction=0.01)

# Run MD for 100 steps
dyn.run(100)

# Get final temperature and energy
final_temp = cu_supercell.get_temperature()
final_energy = cu_supercell.get_potential_energy()

# Print results
print(f"Initial temperature: {init_temp:.2f} K")
print(f"Initial energy: {init_energy:.4f} eV")
print(f"Final temperature: {final_temp:.2f} K")
print(f"Final energy: {final_energy:.4f} eV")

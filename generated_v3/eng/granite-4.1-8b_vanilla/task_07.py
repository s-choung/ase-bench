from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocitydistribution import VelocityVerlet
from ase.units import Ang, fs
import numpy as np

# Create Cu FCC bulk structure
a = 3.615 * Ang
atoms = Atoms('Cu', positions=[[0, 0, 0],
                                 [a/2, a/2, 0],
                                 [a/2, 0, a/2],
                                 [0, a/2, a/2]],
              cell=[a, a, a],
              pbc=True)

# Set up EMT calculator
atoms.calc = EMT()

# Equilibrate velocities at 300 K
MaxwellBoltzmannDistribution(atoms, temperature=300)

# Run NVE MD with VelocityVerlet integrator for 50 steps
nsteps = 50
timestep = 1 * fs
md = VelocityVerlet(atoms, timestep)
for step in range(nsteps):
    md.run(1)

# Compute and print initial and final total energies
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {initial_energy:.3f} eV")
print(f"Final total energy: {final_energy:.3f} eV")

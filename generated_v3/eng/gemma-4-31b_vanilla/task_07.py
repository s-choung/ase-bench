import numpy as np
from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.temperature import MaxwellBoltzmannDistribution

# Setup Cu FCC bulk
atoms = bulk('Cu', 'fcc', a=3.61)
atoms.calc = EMT()

# Initial temperature setup
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# MD setup
dyn = VelocityVerlet(atoms, timestep=2.0 * 1e-15) # 2 fs

def print_energy():
    epot = atoms.get_potential_energy()
    ekin = atoms.get_kinetic_energy()
    print(f"Total Energy: {epot + ekin:.4f} eV")

print("Initial Energy:")
print_energy()

# Run for 50 steps
dyn.run(50)

print("Final Energy:")
print_energy()

from ase import Atoms
from ase.build import fcc111
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
import numpy as np

# Create Pd FCC 2x2x2 supercell
atoms = Atoms('Pd', positions=[[0, 0, 0]], cell=[2.75, 2.75, 2.75], pbc=True)
atoms *= (2, 2, 2)
atoms.calc = EMT()

# Set initial velocities for 500 K
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Record initial total energy
ekin0 = atoms.get_kinetic_energy()
epot0 = atoms.get_potential_energy()
etot0 = ekin0 + epot0

# Run NVE MD with VelocityVerlet
md = VelocityVerlet(atoms, dt=2.0)
for _ in range(200):
    md.run(1)

# Record final total energy
ekinf = atoms.get_kinetic_energy()
epotf = atoms.get_potential_energy()
etotf = ekinf + epotf

# Print energy difference
print(etotf - etot0)

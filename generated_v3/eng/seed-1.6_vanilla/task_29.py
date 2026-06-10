from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet, MaxwellBoltzmannDistribution
import ase.units as units

# Build Pd 2x2x2 FCC supercell
atoms = bulk('Pd', 'fcc').repeat((2,2,2))
atoms.calc = EMT()

# Initialize velocities and get initial total energy
MaxwellBoltzmannDistribution(atoms, 500)
e_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# Run NVE MD
md = VelocityVerlet(atoms, timestep=2*units.fs)
md.run(200)

# Calculate and print energy difference
e_fin = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(e_fin - e_init)

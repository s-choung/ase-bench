from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.io import write
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
import ase.units as u

# Create FCC Pd supercell
atoms = bulk("Pd", "fcc", a=3.9).repeat(2)
atoms.calc = EMT()

# Initialize temperature
MaxwellBoltzmannDistribution(atoms, temperature_K=500)

# Store initial energy
E0 = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Run dynamics
dyn = VelocityVerlet(atoms, timestep=2*u.fs)
dyn.run(steps=200)

# Final energy difference
E_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Energy drift: {E_final - E0:.6f} eV")

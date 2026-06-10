from ase import Atoms
from ase.calculators.lj import LennardJones
from ase.constraints import FixAtoms
from ase.md.langevin import Langevin
from ase.lattice.cubic import FaceCenteredCubic
import numpy as np

# Create Cu FCC bulk 2x2x2 supercell
size = (2, 2, 2)
Cu_lattice = 3.615  # Angstrom, Cu lattice constant
atoms = FaceCenteredCubic(size=size, symbol='Cu', latticeconstant=Cu_lattice)

# Set calculator (Lennard-Jones is not typical for Cu, but used here as per instruction)
atoms.calc = LennardJones(sigma=2.0, epsilon=0.1, rcut=5.0)

# Fix atoms except one degree of freedom for Langevin dynamics
mask = [True] * len(atoms)
atoms.set_constraint(FixAtoms(mask=mask))

# Set up Langevin MD
langevin = Langevin(atoms, 300 * 10**-3 * 314, 1 * 10**-3, 5 * 10**-15)
langevin.run(100)

# Function to calculate temperature and energy
def get_temperature_energy(atoms):
    energy = atoms.get_potential_energy()
    kinetic = atoms.get_kinetic_energy()
    temperature = 2 * kinetic / (3 * len(atoms)) * (1.0 / 6.241509e18)  # Convert to Kelvin
    return temperature, energy

# Print initial temperature and energy
initial_temperature, initial_energy = get_temperature_energy(atoms)
print(f"Initial Temperature: {initial_temperature:.2f} K")
print(f"Initial Energy: {initial_energy:.2f} eV")

# Print final temperature and energy after dynamics
final_temperature, final_energy = get_temperature_energy(atoms)
print(f"Final Temperature: {final_temperature:.2f} K")
print(f"Final Energy: {final_energy:.2f} eV")

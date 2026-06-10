from ase.cluster import Icosahedron
from ase.calculators.emt import EMT
from ase.optimize import BFGS

# Create a gold icosahedral nanoparticle with 3 shells
atom = Icosahedron('Au', noshells=3)

# Print the number of atoms
print(f"Number of atoms: {len(atom)}")

# Print the center of mass
print(f"Center of mass: {atom.get_center_of_mass()}")

# Set up EMT calculator and optimize the structure
atom.calc = EMT()
dyn = BFGS(atom)
dyn.run(fmax=0.05)  # Optimizing until maximum force is below 0.05 eV/Å

# After optimization, print the number of atoms and center of mass again (optional)
print(f"Number of atoms after optimization: {len(atom)}")  # Should be the same
print(f"Center of mass after optimization: {atom.get_center_of_mass()}")

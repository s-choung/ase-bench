from ase import Atoms
from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

# Create the slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Define OH molecule
oh = molecule('OH')

# Define positions for adsorption
positions = ['ontop', 'bridge', 'fcc']

# Calculate energies for each adsorption site
energies = {}
for pos in positions:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=1.2, position=pos)
    slab_copy.calc = EMT()
    energies[pos] = slab_copy.get_potential_energy()

# Find the site with the lowest energy
lowest_site = min(energies, key=energies.get)

# Print the results
for pos in positions:
    print(f"Energy at {pos}: {energies[pos]:.4f} eV")
print(f"Lowest energy site: {lowest_site} with energy {energies[lowest_site]:.4f} eV")

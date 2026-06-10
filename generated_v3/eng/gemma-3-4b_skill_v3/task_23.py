from ase import Atoms
from ase.build import fcc111, add_adsorbate, fcc100, fcc110
from ase.calculators.emt import EMT
from ase.io import write
import numpy as np

# Define the slab dimensions and vacuum
slab_size = (2, 2, 3)
vacuum = 10.0
a = 3.924 # Pt lattice constant
fc = 3.924 # Pt cell parameter
slab = fcc111('Pt', a=a, size=slab_size, vacuum=vacuum)
slab.calc = EMT()

# Define the OH molecule
co =  Atoms.Bravais('L')
co.cell = np.eye(3)
co.positions = np.array([[0.0, 0.0, 0.0], [1.0, 0.0, 0.0], [0.0, 1.0, 0.0]])
co.symbols = ['H', 'O']

# Define the adsorption sites
sites = ['ontop', 'bridge', 'fcc']

# Calculate the energy for each site
energies = []
for site in sites:
    slab_copy = slab.copy()
    if site == 'ontop':
        add_adsorbate(slab_copy, co, height=2.0, position=site)
    elif site == 'bridge':
        add_adsorbate(slab_copy, co, height=2.0, position=site)
    else:
        add_adsorbate(slab_copy, co, height=2.0, position=site)
    slab_copy.calc = EMT()
    energies.append(slab_copy.get_potential_energy())

# Find the site with the lowest energy
best_site = sites[np.argmin(energies)]

# Print the results
print(f"Energy on ontop site: {energies[0]:.6f} eV")
print(f"Energy on bridge site: {energies[1]:.6f} eV")
print(f"Energy on fcc hollow site: {energies[2]:.6f} eV")

print(f"\nLowest energy site: {best_site}")

# Write the optimized structure to a POSCAR file
write('Pt_OH_slab.poscar', slab)

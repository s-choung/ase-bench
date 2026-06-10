from ase import Atoms
from ase.build import fcc111, molecule
from ase.calculators.emt import EMT
import numpy as np

# Create the Pt(111) slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Create the OH molecule
oh = molecule('OH')

# Define adsorption sites
sites = ['ontop', 'bridge', 'fcc']

energies = []
for site in sites:
    # Copy the slab for each site
    slab_copy = slab.copy()
    
    # Adsorb the OH molecule
    from ase.build import add_adsorbate
    add_adsorbate(slab_copy, oh, height=1.5, position=site)
    
    # Attach the EMT calculator
    slab_copy.calc = EMT()
    
    # Compute the energy
    energy = slab_copy.get_potential_energy()
    energies.append(energy)

# Find the lowest energy site
min_energy = min(energies)
min_index = energies.index(min_energy)
best_site = sites[min_index]
print(f"Energies:")
for site, energy in zip(sites, energies):
    print(f"{site}: {energy:.4f} eV")
print(f"The OH molecule adsorbs most stably at the {best_site} site with an energy of {min_energy:.4f} eV")

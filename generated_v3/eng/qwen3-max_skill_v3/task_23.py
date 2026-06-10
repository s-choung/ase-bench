from ase.build import fcc111, add_adsorbate, molecule
from ase.calculators.emt import EMT

# Create clean Pt(111) slab
slab_clean = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Define adsorption sites
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    # Make a copy of the clean slab
    slab = slab_clean.copy()
    
    # Add OH adsorbate
    oh = molecule('OH')
    add_adsorbate(slab, oh, height=1.5, position=site)
    
    # Attach calculator and compute energy
    slab.calc = EMT()
    energy = slab.get_potential_energy()
    energies[site] = energy

# Find and print the most stable site
most_stable = min(energies, key=energies.get)
print(f"Adsorption energies (eV): {energies}")
print(f"Most stable site: {most_stable} ({energies[most_stable]:.3f} eV)")

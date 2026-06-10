from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)

# Define adsorption sites
sites = ['ontop', 'bridge', 'fcc']

# Store energies
energies = {}

for site in sites:
    # Create OH molecule
    oh = Atoms('OH', positions=[(0,0,0), (0,0,0.97)])
    
    # Copy slab and add adsorbate
    structure = slab.copy()
    add_adsorbate(structure, oh, height=2.0, position=site)
    
    # Attach calculator and compute energy
    structure.calc = EMT()
    energy = structure.get_potential_energy()
    energies[site] = energy
    print(f"{site}: {energy:.3f} eV")

# Find minimum energy site
min_site = min(energies, key=energies.get)
print(f"\nLowest energy site: {min_site} ({energies[min_site]:.3f} eV)")

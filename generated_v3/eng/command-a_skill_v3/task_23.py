from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)

# Create OH molecule
oh = molecule('OH')

# Prepare systems for different adsorption sites
systems = []
for position in ['ontop', 'bridge', 'hollow']:
    slab_copy = slab.copy()
    add_adsorbate(slab_copy, oh, height=1.5, position=position)
    slab_copy.calc = EMT()
    systems.append(slab_copy)

# Compute single-point energies
energies = [system.get_potential_energy() for system in systems]

# Determine lowest energy site
min_energy = min(energies)
min_index = energies.index(min_energy)
sites = ['ontop', 'bridge', 'hollow']
print(f"Lowest energy site: {sites[min_index]} with energy {min_energy:.4f} eV")

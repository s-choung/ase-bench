from ase.build import bulk, fcc111, molecule, add_adsorbate
from ase.constraints import FixAtoms
from ase.calculators.emt import EMT

# Create a Pt(111) 3-layer slab
slab_size = (3, 3, 3)  # Larger supercell for different adsorption sites
vacuum = 10.0
slab = fcc111('Pt', size=slab_size, a=3.92, vacuum=vacuum)

# Create OH molecule
oh = molecule('OH')

# Define adsorption sites
adosorption_sites = {
    'ontop': {'position': 'ontop', 'height': 2.2},
    'bridge': {'position': 'bridge', 'height': 2.0, 'offset': (0.25, 0.25, 0)},
    'fcc': {'position': 'fcc', 'height': 2.0, 'offset': (0.5, 0.5, 0)}
}

# Function to calculate energy for a given adsorption site
def get_energy(slab, oh, site_info):
    adsorbate = oh.copy()
    add_adsorbate(slab, adsorbate, height=site_info['height'],
                  position=site_info['position'], offset=site_info.get('offset', (0, 0, 0)))
    slab.set_constraint(FixAtoms(mask=[atom.tag >= 3 for atom in slab]))  # Fix bottom layer
    slab.calc = EMT()
    energy = slab.get_potential_energy()
    slab.set_positions([position - [0, 0, 3] for position in slab.get_positions()])  # Restore original positions
    return energy

# Compute energies for each site
energies = {}
for site, site_info in adosorption_sites.items():
    energies[site] = get_energy(slab.copy(), oh, site_info)

# Determine the site with the lowest energy
min_site = min(energies, key=energies.get)
min_energy = energies[min_site]

# Print results
print("Adsorption Site Energies (eV):")
for site, energy in energies.items():
    print(f"{site}: {energy:.6f}")
print(f"\nThe lowest energy site is {min_site} with an energy of {min_energy:.6f} eV.")

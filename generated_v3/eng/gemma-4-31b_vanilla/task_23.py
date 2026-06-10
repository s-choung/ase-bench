from ase import Atoms
from ase.build import fcc111_slab
from ase.calc.emt import EMT

def get_energy(site_type):
    slab = fcc111_slab('Pt', size=(2, 2, 3), vacuum=10.0)
    
    # Define OH geometry (O-H bond length ~0.97 A)
    oh = Atoms('OH', positions=[(0, 0, 0), (0, 0, 0.97)])
    
    # Position the O atom based on site
    if site_type == 'ontop':
        # Pt atom at (0,0,z)
        pos = slab.positions[0]
    elif site_type == 'bridge':
        # Midpoint between two surface Pt atoms
        pos = (slab.positions[0] + slab.positions[1]) / 2
    elif site_type == 'fcc':
        # Center of three surface atoms (approximate hollow)
        pos = (slab.positions[0] + slab.positions[1] + slab.positions[4]) / 3
    
    # Adjust height: place O approx 1.8 A above the surface site
    pos[2] += 1.8
    oh.positions[0] = pos
    oh.positions[1] = pos + [0, 0, 0.97]
    
    combined = slab + oh
    combined.calc = EMT()
    return combined.get_potential_energy()

sites = ['ontop', 'bridge', 'fcc']
energies = {site: get_energy(site) for site in sites}

for site, energy in energies.items():
    print(f"{site}: {energy:.4f} eV")

best_site = min(energies, key=energies.get)
print(f"Lowest energy site: {best_site}")

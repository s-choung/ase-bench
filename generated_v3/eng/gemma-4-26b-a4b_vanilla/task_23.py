from ase.build import fcc111, add_adsorbate
from ase.io import read
from ase.calculators.emt import EMT
from ase.units import eV

def get_energy(site_type, pos):
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    # pos is (x, y, z) relative to slab surface
    # Adjust z to be above the surface (z=0 is the surface plane in fcc111)
    # For Pt, the top layer is at z=0. We place OH at height ~2.0
    add_adsorbate(slab, 'OH', height=2.0, position=pos)
    slab.calc = EMT()
    return slab.get_potential_energy()

# Define sites on a 3x3 surface unit cell
# Pt-Pt distance ~2.77 A
sites = {
    'ontop': (0.0, 0.0),
    'bridge': (1.385, 0.0),
    'fcc_hollow': (0.857, 0.5) # Approx center of triangle
}

results = {}
for name, coord in sites.items():
    # We use specific coords relative to the lattice vectors
    # To simplify, we'll just use ASE's add_adsorbate logic 
    # with site types directly if possible, but manual is more precise.
    # Re-defining via add_adsorbate site parameter:
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    add_adsorbate(slab, 'OH', height=2.0, position=coord, char='O') # Simplified
    # Actually, standard ASE add_adsorbate takes 'ontop', 'bridge', 'fcc', 'hcp'
    
    # Correct approach using ASE built-in site naming
    slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0)
    add_adsorbate(slab, 'OH', height=2.0, position=name)
    slab.calc = EMT()
    results[name] = slab.get_potential_energy()

print("Energies (eV):", results)
best_site = min(results, key=results.get)
print(f"Lowest energy site: {best_site}")

from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from copy import deepcopy
from ase import Atoms

# Create 3-layer Pt(111) slab with 10Å vacuum, 4x4 surface to avoid periodic adsorbate interactions
pt_lattice = 3.92  # Experimental fcc lattice constant for Pt
base_slab = fcc111('Pt', size=(4, 4, 3), vacuum=10.0, latticeconstant=pt_lattice)

# Define OH adsorbate (O at origin, H 0.95Å above, O binds to Pt surface)
oh_adsorbate = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.95]])

# Define high-symmetry adsorption sites (fractional surface cell coordinates)
adsorption_sites = {
    'ontop': (0.0, 0.0),
    'bridge': (0.5, 0.0),
    'fcc_hollow': (1/3, 1/3)
}

# Calculate single-point energies for each site
site_energies = {}
for site, frac in adsorption_sites.items():
    # Create independent slab copy for each adsorption site
    slab = deepcopy(base_slab)
    # Convert fractional coordinates to cartesian surface coordinates
    x_pos = frac[0] * slab.cell[0, 0] + frac[1] * slab.cell[1, 0]
    y_pos = frac[0] * slab.cell[0, 1] + frac[1] * slab.cell[1, 1]
    # Add OH adsorbate, COM height ~1.2Å above top Pt layer to place O ~1.1Å above Pt
    add_adsorbate(slab, oh_adsorbate, height=1.25, position=(x_pos, y_pos))
    # Attach EMT calculator and compute energy
    slab.calc = EMT()
    site_energies[site] = slab.get_potential_energy()

# Print results and identify lowest energy site
print("OH adsorption single-point energies (eV) on Pt(111):")
for site, energy in site_energies.items():
    print(f"{site:12s} : {energy:.3f}")

lowest_site = min(site_energies, key=site_energies.get)
print(f"\nLowest energy adsorption site: {lowest_site} (energy = {site_energies[lowest_site]:.3f} eV)")

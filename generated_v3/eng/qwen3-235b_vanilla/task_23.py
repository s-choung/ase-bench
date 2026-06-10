from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.center(axis=2)

# Define adsorption sites
sites = ['ontop', 'bridge', 'fcc']
energies = []

for site in sites:
    # Copy clean slab
    system = slab.copy()
    # Add OH adsorbate (use approximate height, adjust if needed)
    add_adsorbate(system, Atoms('OH', positions=[(0, 0, 8.5), (0, 0, 10.0)]), height=1.2, position=site)
    # Connect EMT calculator
    calc = EMT()
    system.calc = calc
    # Compute energy
    energy = system.get_potential_energy()
    energies.append(energy)

# Find lowest energy site
lowest_site = sites[energies.index(min(energies))]
print(f"Lowest energy adsorption site: {lowest_site} ({min(energies):.3f} eV)")

from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import QuasiNewton

# Create a Pt(111) slab with 3 layers
slab = fcc111('Pt', size=(1, 1, 3), vacuum=10.0)

# Constrain the bottom two layers
slab.set_constraint(FixAtoms(mask=[z > 1 for z in slab.positions[:, 2]]))

# Define OH adsorption on different sites
sites = ['ontop', 'bridge', 'fcc']
energies = {}

for site in sites:
    # Create a slab with adsorbate for each site
    system = slab.copy()
    add_adsorbate(system, 'OH', 1.8, site)  # 1.8 Angstrom is a typical height for adsorption
    
    # Attach EMT calculator
    system.calc = EMT()
    
    # Optimize the geometry
    dyn = QuasiNewton(system)
    dyn.run(fmax=0.05)
    
    # Compute single-point energy and store it
    energies[site] = system.get_potential_energy()

# Find and print the site with the lowest energy
min_site = min(energies, key=energies.get)
print(f"The lowest energy site is {min_site} with energy {energies[min_site]} eV.")

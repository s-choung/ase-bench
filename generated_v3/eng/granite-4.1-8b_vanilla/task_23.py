from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import slab, add_adsorbate

# Create Pt(111) 3-layer slab
slab = slab('Pt', '111', 3, vacuum=10.0)

# Define OH molecule
oh = Atoms('OH')
oh.center(vacuum=5.0)

# Site positions for OH adsorption
top = [0.5, 0.5, 1.5]
bridge = [0.5, 0.0, 1.25]
fcc_hollow = [0.25, 0.5, 1.5]

# Adsorb OH on each site
slab_top = add_adsorbate(slab, oh, top)
slab_bridge = add_adsorbate(slab, oh, bridge)
slab_fcc_hollow = add_adsorbate(slab, oh, fcc_hollow)

# Attach EMT calculator to each structure
for atoms in [slab_top, slab_bridge, slab_fcc_hollow]:
    atoms.set_calculator(EMT())

# Compute single-point energies
energies = {}
energies['top'] = slab_top.get_potential_energy()
energies['bridge'] = slab_bridge.get_potential_energy()
energies['fcc_hollow'] = slab_fcc_hollow.get_potential_energy()

# Compare and print the lowest energy site
lowest_energy_site = min(energies, key=energies.get)
print(f"Site with the lowest energy: {lowest_energy_site} with energy {energies[lowest_energy_site]:.6f} eV")

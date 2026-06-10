from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

# Create Pt(111) 3-layer slab
slab = fcc111('Pt', size=(1,1,3), vacuum=10.0)

# Create OH molecule
oh = Atoms('OH', positions=[[0., 0., 0.], [0., 0., 0.97]])

# Add OH to each site
slab_ontop = slab.copy()
add_adsorbate(slab_ontop, oh, height=1.8, position='ontop')

slab_bridge = slab.copy()
add_adsorbate(slab_bridge, oh, height=1.8, position='bridge')

slab_fcc = slab.copy()
add_adsorbate(slab_fcc, oh, height=1.8, position='fcc')

# Attach EMT calculator and compute energies
slab_ontop.calc = EMT()
energy_ontop = slab_ontop.get_potential_energy()

slab_bridge.calc = EMT()
energy_bridge = slab_bridge.get_potential_energy()

slab_fcc.calc = EMT()
energy_fcc = slab_fcc.get_potential_energy()

# Compare energies
energies = {'ontop': energy_ontop, 'bridge': energy_bridge, 'fcc': energy_fcc}
min_site = min(energies, key=energies.get)
print(f"Lowest energy site: {min_site} with energy {energies[min_site]} eV")

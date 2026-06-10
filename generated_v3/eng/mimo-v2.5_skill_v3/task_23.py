from ase.build import fcc111, molecule, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

# Create base Pt(111) slab with 3 layers and 10 Å vacuum
slab = fcc111('Pt', size=(3, 3, 3), vacuum=10.0, a=3.92)

# Fix bottom two layers (layers 0 and 1) for all slabs
constraint = FixAtoms(mask=[atom.tag < 2 for atom in slab])

# Create OH molecule
oh = molecule('OH')

# Store energies for each site
energies = {}

# Test ontop site
slab_ontop = slab.copy()
add_adsorbate(slab_ontop, oh, height=1.8, position='ontop')
slab_ontop.set_constraint(constraint)
slab_ontop.calc = EMT()
energies['ontop'] = slab_ontop.get_potential_energy()

# Test bridge site
slab_bridge = slab.copy()
add_adsorbate(slab_bridge, oh, height=1.5, position='bridge')
slab_bridge.set_constraint(constraint)
slab_bridge.calc = EMT()
energies['bridge'] = slab_bridge.get_potential_energy()

# Test fcc hollow site
slab_fcc = slab.copy()
add_adsorbate(slab_fcc, oh, height=1.0, position='fcc')
slab_fcc.set_constraint(constraint)
slab_fcc.calc = EMT()
energies['fcc'] = slab_fcc.get_potential_energy()

# Find and print lowest energy site
min_site = min(energies, key=energies.get)
print("Energies (eV) for OH adsorption on Pt(111):")
for site, energy in energies.items():
    print(f"  {site}: {energy:.4f} eV")
print(f"\nLowest energy site: {min_site} with {energies[min_site]:.4f} eV")

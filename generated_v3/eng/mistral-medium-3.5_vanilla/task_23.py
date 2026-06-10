from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms

slab = fcc111('Pt', size=(3, 3, 3), vacuum=10)
slab.calc = EMT()

ontop = slab.copy()
add_adsorbate(ontop, Atoms('OH', positions=[[0, 0, 0]]), height=1.5, position=(0, 0))
ontop.calc = EMT()
e_ontop = ontop.get_potential_energy()

bridge = slab.copy()
add_adsorbate(bridge, Atoms('OH', positions=[[0, 0, 0]]), height=1.5, position=(0.5, 0))
bridge.calc = EMT()
e_bridge = bridge.get_potential_energy()

fcc = slab.copy()
add_adsorbate(fcc, Atoms('OH', positions=[[0, 0, 0]]), height=1.5, position=(0.5, 0.5/3))
fcc.calc = EMT()
e_fcc = fcc.get_potential_energy()

sites = ['ontop', 'bridge', 'fcc']
energies = [e_ontop, e_bridge, e_fcc]
min_site = sites[energies.index(min(energies))]
print(f"Lowest energy site: {min_site} ({min(energies):.2f} eV)")

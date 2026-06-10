from ase.build import fcc111, add_adsorbate
from ase import Atoms
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
oh = Atoms('OH', positions=[[0., 0., 0.], [0., 0., 1.0]], pbc=False)

slab_ontop = slab.copy()
slab_bridge = slab.copy()
slab_fcc = slab.copy()

add_adsorbate(slab_ontop, oh, height=1.8, position='ontop')
add_adsorbate(slab_bridge, oh, height=1.8, position='bridge')
add_adsorbate(slab_fcc, oh, height=1.8, position='fcc')

for atoms in [slab_ontop, slab_bridge, slab_fcc]:
    atoms.calc = EMT()

ontop = slab_ontop.get_potential_energy()
bridge = slab_bridge.get_potential_energy()
fcc = slab_fcc.get_potential_energy()

print(f'Energies: ontop={ontop:.3f}, bridge={bridge:.3f}, fcc={fcc:.3f}')
min_e = min(ontop, bridge, fcc)
print('Lowest energy site: ' + ('ontop' if min_e == ontop else 'bridge' if min_e == bridge else 'fcc'))

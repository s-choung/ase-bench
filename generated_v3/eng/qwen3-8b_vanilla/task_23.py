import ase.build as ab
from ase.calculators.emt import EMT
from ase import Atoms

# Create Pt(111) 3-layer slab
slab = ab.fcc111('Pt', size=(1,1,3), a=3.92, vacuum=10.0)

def add_OH(slab, pos):
    O = Atoms('O', positions=[pos])
    H = Atoms('H', positions=[pos + (0,0,1.5)])
    return slab + O + H

# On-top site
top_pos = slab[-1].position
slab_ontop = add_OH(slab, top_pos)

# Bridge site
bridge_pos = (slab[-1].position + slab[-2].position) / 2
slab_bridge = add_OH(slab, bridge_pos)

# FCC hollow site
fcc_pos = (slab[-1].position + slab[-2].position + slab[-3].position) / 3
slab_fcc = add_OH(slab, fcc_pos)

def calc_energy(s):
    s.calc = EMT()
    return s.get_potential_energy()

e_ontop = calc_energy(slab_ontop)
e_bridge = calc_energy(slab_bridge)
e_fcc = calc_energy(slab_fcc)

energies = {'ontop': e_ontop, 'bridge': e_bridge, 'fcc': e_fcc}
min_site = min(energies, key=energies.get)
print(f"Lowest energy site: {min_site} with energy {energies[min_site]}")

from ase.build import fcc111, add_adsorbate
from ase.molecules import molecule
from ase.calculators.emt import EMT

slab = fcc111('Al', size=(1, 1, 3), a=4.05, vacuum=10.0)
add_adsorbate(slab, molecule('N2'), position='bridge', layers=1)

n_indices = [i for i, symbol in enumerate(slab.get_chemical_symbols()) if symbol == 'N']
for i in n_indices:
    pos = slab.get_positions()[i]
    pos[2] += 2.0
    slab.set_positions(pos, indices=[i])

slab.set_calculator(EMT())
print(len(slab), slab.get_chemical_symbols())

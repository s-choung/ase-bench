from ase.build import molecule
from ase.calculators.emt import EMT
from ase.io import write

slab = molecule('N2')
slab.add_adsorbate(position=[0.5, 0.5, 2.0], site='bridge')
slab.vacuum = 10.0

calc = EMT()
slab.set_calculator(calc)
calc.xc = 'gga'
slab.get_projection()

print(f"Number of atoms: {len(slab)}")
print(f"Atom types: {slab.get_element()}")
write('al111_n2.xyz', slab)

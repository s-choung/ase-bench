from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT

slab = fcc111('Pt', size=(4, 4, 4), vacuum=10.0)
co = add_adsorbate(slab, 'CO', height=2.0, position='ontop')

calc = EMT()
co.set_calculator(calc)
energy = co.get_potential_energy()

print(len(co))

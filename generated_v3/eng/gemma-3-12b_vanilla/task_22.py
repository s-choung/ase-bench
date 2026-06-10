from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import write

slab = fcc111('Al', (3, 3, 3), vacuum=10.0)
n2 = ase.build.molecule('N2')
n2.set_initial_potential_energy(0.0)

add_adsorbate(slab, n2, site='bridge', height=2.0)

calc = EMT()
slab.calc = calc

print(f"Number of atoms: {len(slab.get_atomic_numbers())}")
print(f"Atom types: {sorted(list(set(slab.get_atomic_numbers())))}")

write('Al_N2_slab.xyz', slab)

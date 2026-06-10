from ase import units
from ase.calculators.emt import EMT
from ase.build import fcc111, add_adsorbate, molecule

sites = ['ontop', 'bridge', 'fcc']
energies = []

for pos in sites:
    slab = fcc111('Pt', size=(2,2,3), vacuum=10.0)
    OH = molecule('OH', vacuum=4.0)  # Pre-create with spacing
    slab.calc = EMT()
    add_adsorbate(slab, OH, height=1.5, position=pos)
    slab.set_constraint(FixAtoms(mask=[a.tag > 2 for a in slab]))
    energies.append(slab.get_potential_energy())

min_idx = energies.index(min(energies))
print(f"{sites[min_idx]} has lowest energy: {energies[min_idx]:.3f} eV")

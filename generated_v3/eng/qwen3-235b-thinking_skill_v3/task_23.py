from ase.build import fcc111, molecule
from ase.calculators.lj import LennardJones
from ase.constraints import FixAtoms
from ase.build import add_adsorbate

sites = ['ontop', 'bridge', 'fcc']
energies = []

params = {
    ('H', 'H'): {'epsilon': 0.1, 'sigma': 1.2},
    ('H', 'O'): {'epsilon': 0.4, 'sigma': 1.5},
    ('H', 'Pt'): {'epsilon': 0.1, 'sigma': 1.8},
    ('O', 'O'): {'epsilon': 0.2, 'sigma': 3.0},
    ('O', 'Pt'): {'epsilon': 0.5, 'sigma': 2.2},
    ('Pt', 'Pt'): {'epsilon': 1.0, 'sigma': 2.5}
}
calc = LennardJones(parameters=params, rc=5.0)

for site in sites:
    slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
    slab.set_constraint(FixAtoms(mask=[a.tag >= 2 for a in slab]))
    add_adsorbate(slab, molecule('OH'), height=1.9, position=site)
    slab.calc = calc
    energies.append(slab.get_potential_energy())

for i, e in enumerate(energies):
    print(f"{sites[i]} energy: {e:.6f} eV")
min_idx = energies.index(min(energies))
print(f"The {sites[min_idx]} site has the lowest energy.")

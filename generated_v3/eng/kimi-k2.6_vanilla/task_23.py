from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase import Atoms
from ase.constraints import FixAtoms

oh = Atoms('OH', positions=[[0, 0, 0], [0, 0, 0.98]])
base = fcc111('Pt', size=(2, 2, 3), a=3.92, vacuum=10.0)
base.set_constraint(FixAtoms(indices=[i for i, t in enumerate(base.get_tags()) if t > 1]))

energies = {}
for site in ['ontop', 'bridge', 'fcc']:
    slab = base.copy()
    slab.calc = EMT()
    add_adsorbate(slab, oh, height=1.5, site=site)
    energies[site] = slab.get_potential_energy()
    print(f"{site:6s}: {energies[site]:.4f} eV")

best = min(energies, key=energies.get)
print(f"Lowest energy site: {best}")

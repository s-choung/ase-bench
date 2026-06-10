from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase import Atom
from ase.io import write
import numpy as np

slab = fcc111('Pt', size=(2, 2, 3), vacuum=10.0)
slab.set_constraint(FixAtoms(indices=[atom.index for atom in slab if atom.tag == 3]))

sites = {
    'ontop': (0.0, 0.0),
    'bridge': (0.5 * slab.cell[0, 0], 0.0),
    'fcc': (1.0 / 3.0 * slab.cell[0, 0], 1.0 / 3.0 * slab.cell[1, 1]),
}

results = {}

for site, pos in sites.items():
    atoms = slab.copy()
    add_adsorbate(atoms, 'O', height=1.8, position=site)
    o_idx = len(atoms) - 1
    o_pos = atoms[o_idx].position.copy()
    h_pos = o_pos + np.array([0.0, 0.0, 0.97])
    atoms.append(Atom('H', position=h_pos))
    atoms.calc = EMT()
    e = atoms.get_potential_energy()
    results[site] = e
    print(f"{site}: {e:.6f} eV")

best = min(results, key=results.get)
print(f"Lowest energy site: {best} ({results[best]:.6f} eV)")

import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase import Atoms
from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.io import write

sites = ["ontop", "bridge", "fcc"]
energies = {}

for site in sites:
    slab = fcc111("Pt", size=(3, 3, 3), vacuum=10.0)
    oh = Atoms("OH", positions=[(0.0, 0.0, 0.0), (0.0, 0.0, 0.97)])
    add_adsorbate(slab, oh, height=1.8, position=site)
    slab.calc = EMT()
    energy = slab.get_potential_energy()
    energies[site] = energy
    write(f"Pt111_OH_{site}.xyz", slab)

for site, energy in energies.items():
    print(f"{site:6s}: {energy:.6f} eV")

best_site = min(energies, key=energies.get)
print(f"Lowest energy site: {best_site} ({energies[best_site]:.6f} eV)")


def _dump_structure(_path):
    try:
        from ase import Atoms as _A
        from ase.io import write as _w
        g = dict(globals())
        cands = [v for v in g.values() if isinstance(v, _A) and len(v) > 0]
        for v in g.values():
            if isinstance(v, (list, tuple)) and v and all(isinstance(x, _A) for x in v):
                cands.append(max(v, key=len))
        if not cands:
            print("XYZ_NONE"); return
        best = max(cands, key=lambda a: len(a))
        # ensure a cell for molecules so the viewer frames sensibly
        _w(_path, best)
        print("XYZ_WROTE", len(best), best.get_chemical_formula())
    except Exception as _e:
        print("XYZ_FAIL", repr(_e))

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T23.xyz')

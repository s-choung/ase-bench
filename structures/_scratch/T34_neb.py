import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase.build import fcc111, add_adsorbate
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS
import numpy as np

a = 3.615
size = (2, 2, 4)
vacuum = 10.0
height = 2.0

initial = fcc111('Cu', size=size, a=a, vacuum=vacuum)
initial.set_constraint(FixAtoms(mask=[atom.tag > 2 for atom in initial]))
add_adsorbate(initial, 'Cu', height=height, position='fcc')

final = initial.copy()
xy = final.get_positions()[-1, :2].copy()
cell = final.get_cell()
shift = (cell[0, :2] + cell[1, :2]) / 3.0
final.positions[-1, :2] = xy + shift

images = [initial] + [initial.copy() for _ in range(5)] + [final]
for img in images:
    img.calc = EMT()

neb = NEB(images)
neb.interpolate(method='idpp')

opt = BFGS(neb, logfile=None, trajectory=None)
opt.run(fmax=0.05)

energies = [img.get_potential_energy() for img in images]
barrier = max(energies) - energies[0]
print(barrier)

def _dump_overlay(_path):
    try:
        from ase import Atoms as _A
        from ase.io import write as _w
        g = dict(globals())
        bands = [v for v in g.values()
                 if isinstance(v, (list, tuple)) and len(v) >= 3
                 and all(isinstance(x, _A) for x in v)]
        if not bands:
            print("NEB_NONE"); return
        band = max(bands, key=len)
        combined = band[0].copy()
        for img in band[1:]:
            combined += img
        combined.set_pbc(False)
        _w(_path, combined)
        print("NEB_WROTE", len(band), "images ->", len(combined), "atoms")
    except Exception as _e:
        print("NEB_FAIL", repr(_e))

_dump_overlay('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T34.xyz')

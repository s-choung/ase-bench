import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.mep import NEB
from ase.optimize import BFGS

initial = Atoms(
    "Al3",
    positions=[
        [0.0, 0.0, 0.0],
        [5.0, 0.0, 0.0],
        [2.5, -1.5, 0.0],
    ],
)

final = Atoms(
    "Al3",
    positions=[
        [0.0, 0.0, 0.0],
        [5.0, 0.0, 0.0],
        [2.5, 1.5, 0.0],
    ],
)

constraint = FixAtoms(indices=[0, 1])
initial.set_constraint(constraint)
final.set_constraint(constraint)

images = [initial] + [initial.copy() for _ in range(3)] + [final]
neb = NEB(images)
neb.interpolate(method="linear")

for image in images:
    image.calc = EMT()

opt = BFGS(neb, logfile=None)
opt.run(fmax=0.05, steps=100)

for i, image in enumerate(images):
    print(i, image.get_potential_energy())

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

_dump_overlay('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T35.xyz')

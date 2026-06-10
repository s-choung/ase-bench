import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from pathlib import Path
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.db import connect

dbfile = "cu_ag_au_emt.db"
Path(dbfile).unlink(missing_ok=True)

db = connect(dbfile)

for symbol, a in [("Cu", 3.60), ("Ag", 4.09), ("Au", 4.08)]:
    atoms = bulk(symbol, "fcc", a=a)
    atoms.calc = EMT()
    atoms.get_potential_energy()
    db.write(atoms, metal=symbol)

for row in db.select():
    print(row.formula, row.energy)


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T42.xyz')

import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.filters import FrechetCellFilter
from ase.optimize.precon import PreconLBFGS

atoms = bulk("Ni", "fcc", a=3.52, cubic=True)
atoms.calc = EMT()

opt = PreconLBFGS(FrechetCellFilter(atoms), precon="auto")
opt.run(fmax=0.01)

cellpar = atoms.cell.cellpar()
energy = atoms.get_potential_energy()
steps = opt.get_number_of_steps()

print(f"Steps: {steps}")
print(f"Final energy: {energy:.8f} eV")
print(f"Cell parameters: a={cellpar[0]:.6f} Å, b={cellpar[1]:.6f} Å, c={cellpar[2]:.6f} Å, "
      f"alpha={cellpar[3]:.6f}°, beta={cellpar[4]:.6f}°, gamma={cellpar[5]:.6f}°")


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T26.xyz')

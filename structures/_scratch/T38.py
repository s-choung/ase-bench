import matplotlib
matplotlib.use('Agg')
import warnings; warnings.filterwarnings('ignore')
try:
 import ase.visualize as _vis
 _vis.view=lambda *a,**k:None
except Exception:
 pass

import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo

atoms = bulk("Cu", "fcc", a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

BFGS(FrechetCellFilter(atoms), logfile=None).run(fmax=0.01)

vib = Vibrations(atoms, name="cu_bulk_vib")
vib.run()

freqs = vib.get_frequencies()
vib_energies = np.real(vib.get_energies())
vib_energies = vib_energies[vib_energies > 1e-5]

thermo = HarmonicThermo(vib_energies=vib_energies, potentialenergy=atoms.get_potential_energy())
F = thermo.get_helmholtz_energy(temperature=300.0, verbose=False)

print("F_helmholtz_300K_eV =", F)

vib.clean()


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

_dump_structure('/Users/sean/Library/CloudStorage/GoogleDrive-wjdtjrgus9967@gmail.com/My Drive/Research_2026/playground/108_ase_skill/benchmark/structures/T38.xyz')

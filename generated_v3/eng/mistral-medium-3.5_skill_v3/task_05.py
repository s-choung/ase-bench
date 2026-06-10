from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState
import numpy as np

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.001)

cell = atoms.get_cell()
volumes, energies = [], []
for scale in np.linspace(0.95, 1.05, 7):
    a = atoms.copy()
    a.set_cell(cell * scale, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
print(f"Equilibrium volume: {v0:.3f} Å³")
print(f"Bulk modulus: {B/units.GPa:.1f} GPa")

import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.eos import EquationOfState

# 1. EOS for FCC Cu bulk
atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()
volumes, energies = [], []
a0 = 3.6
ratios = np.linspace(0.96, 1.04, 7)
for r in ratios:
    a = atoms.copy()
    a.set_cell(cell * (r,), scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = a0 * (v0 / atoms.get_volume()) ** (1/3)

# 2. Build Cu(111) slab (4 layers)
slab = fcc111('Cu', size=(2,2,4), vacuum=10.0, a=a_eq)
# 3. Attach EMT calculator
slab.calc = EMT()
# 4. Fix bottom 2 layers
zs = slab.positions[:,2]
unique_z = np.unique(np.round(zs, 6))
# bottom 2 layers: min 2 z
zlayers = np.sort(unique_z)
mask = np.isin(np.round(zs,6), zlayers[:2])
from ase.constraints import FixAtoms
slab.set_constraint(FixAtoms(mask=mask))
# 5. Surface relaxation
opt = BFGS(slab)
opt.run(fmax=0.05)

# 6. Print final energy and average z for each layer
print('Final energy (eV):', slab.get_potential_energy())
zs = slab.positions[:,2]
zlayers = np.sort(np.unique(np.round(zs, 6)))
for i, zval in enumerate(zlayers):
    idxs = np.where(np.abs(zs-zval) < 1e-5)[0]
    meanz = zs[idxs].mean()
    print(f'Layer {i+1}: avg z = {meanz:.4f} Å, atoms = {idxs.tolist()}')

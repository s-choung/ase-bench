import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS

# 1. Equilibrium lattice constant via EOS
atoms = bulk('Cu', 'fcc', a=3.6)
cell = atoms.get_cell()
vols, ens = [], []
for x in np.linspace(0.95, 1.05, 7):
    s = atoms.copy()
    s.set_cell(cell * x, scale_atoms=True)
    s.calc = EMT()
    vols.append(s.get_volume())
    ens.append(s.get_potential_energy())
v0, e0, B = EquationOfState(vols, ens).fit()
a_eq = v0 ** (1/3)
print(f"a_eq = {a_eq:.4f} Å, B = {B:.2f} eV/Å^3")

# 2. (111) slab, 4 layers
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
z0 = slab.positions[:, 2].copy()
zlayers = np.sort(np.unique(np.round(z0, 2)))

# 3. Fix bottom 2 layers
fix = np.isin(np.round(z0, 2), zlayers[:2])
slab.set_constraint(FixAtoms(mask=fix))
slab.calc = EMT()

# 4. BFGS surface relaxation
BFGS(slab).run(fmax=0.05)

# 5. Report
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
for i, z in enumerate(zlayers):
    idx = np.where(np.isclose(z0, z, atol=0.1))[0]
    print(f"Layer {i+1}: <z> = {slab.positions[idx, 2].mean():.4f} Å")

from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
import numpy as np

# 1. bulk Cu (fcc)
bulk = bulk('Cu', 'fcc', a=3.5)          # placeholder a
bulk.calc = EMT()

# 2. EOS fitting to obtain equilibrium lattice constant
cell = bulk.get_cell()
volumes = []
energies = []
for x in np.linspace(0.95, 1.05, 7):
    slab = bulk.copy()
    slab.set_cell(cell * x, scale_atoms=True)
    slab.calc = EMT()
    volumes.append(slab.get_volume())
    energies.append(slab.get_potential_energy())
from ase.eos import EquationOfState
eos = EquationOfState(volumes, energies, eos='sipr')
a_eq, e0, B = eos.fit()
bulk.set_cell(np.diag([a_eq, a_eq, a_eq]), scale_atoms=True)

print(f"Equilibrium lattice constant of Cu (fcc): a_eq = {a_eq:.4f} Å")

# 3. construct 111 slab (4 layers, vacuum 10 Å)
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# 4. fix bottom two layers
from ase.constraints import FixAtoms
fix_mask = [slab[i].tag >= 2 for i in range(len(slab))]
fix = FixAtoms(mask=fix_mask)
slab.set_constraint(fix)

# 5. surface relaxation with BFGS (FrechetCellFilter includes vacuum)
opt = BFGS(FrechetCellFilter(slab))
opt.run(fmax=0.02)

# 6. final volume, energy, and average z of each layer
V_final = slab.get_volume()
E_final = slab.get_potential_energy()
z_vals = slab.positions[:, 2]          # z‑coordinate of every atom
layer_id = 0
for ar in slab:
    within_layer = z_vals[z_vals >= ar.z - 1e-6]   # atoms in same plateau (approx)
    avg_height = np.mean(within_layer)
    print(f"Layer {layer_id} mid‑plane z ≈ {avg_height:.4f} Å")
    layer_id += 1

print(f"\nFinal energy: {E_final:.4f} eV, volume: {V_final:.4f} Å³")

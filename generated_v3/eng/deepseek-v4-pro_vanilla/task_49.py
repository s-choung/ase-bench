import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms

# ---------- 1. Equilibrium lattice constant via EOS ----------
a_vals = np.linspace(3.5, 3.8, 7)
volumes = []
energies = []
for a in a_vals:
    cu = bulk('Cu', 'fcc', a=a)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = v0 ** (1.0 / 3.0)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")

# ---------- 2. Build (111) 4-layer slab ----------
slab = fcc111('Cu', a=a_eq, size=(1, 1, 4), vacuum=10.0)
slab.calc = EMT()

# ---------- 3. Assign each atom to a layer (bottom = 0, top = 3) ----------
init_z = slab.positions[:, 2]
unique_z = sorted(set(np.round(init_z, decimals=6)))
layers = np.argmin(np.abs(init_z[:, None] - np.array(unique_z)), axis=1)

# ---------- 4. Fix bottom two layers and relax ----------
bottom_mask = [i for i, l in enumerate(layers) if l < 2]
slab.set_constraint(FixAtoms(bottom_mask))
opt = BFGS(slab)
opt.run(fmax=0.01)

# ---------- 5. Output final energy and layer‑wise average z ----------
print(f"Final energy: {slab.get_potential_energy():.6f} eV")
print("Average z‑coordinate per layer:")
for lay in range(4):
    idx = np.where(layers == lay)[0]
    avg_z = slab.positions[idx, 2].mean()
    print(f"Layer {lay}: {avg_z:.4f} Å")

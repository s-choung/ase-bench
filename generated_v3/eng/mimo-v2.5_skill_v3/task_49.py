import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.constraints import FixAtoms
from ase.eos import EquationOfState

# --- Step 1: Find equilibrium lattice constant via EOS ---
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
cell = atoms.get_cell()
volumes, energies = [], []
for s in np.linspace(0.90, 1.10, 11):
    a = atoms.copy()
    a.set_cell(cell * s, scale_atoms=True)
    a.calc = EMT()
    volumes.append(a.get_volume())
    energies.append(a.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1.0 / 3.0)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å  (bulk E₀ = {e0:.4f} eV)")

# --- Step 2: Build 4-layer (111) slab ---
slab = fcc111('Cu', size=(2, 2, 4), a=a_eq, vacuum=10.0)
n_layers = max(a.tag for a in slab) + 1
print(f"Slab: {len(slab)} atoms, {n_layers} layers")

# --- Step 3: Fix bottom 2 layers, attach EMT, relax ---
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag < n_layers // 2 for a in slab]))

opt = BFGS(slab, trajectory='cu111_relax.traj')
opt.run(fmax=0.05)

# --- Step 4: Print final energy and average z per layer ---
print(f"\nFinal energy: {slab.get_potential_energy():.6f} eV")
print("Average z-coordinate per layer:")
for layer in range(n_layers):
    zs = [a.position[2] for a in slab if a.tag == layer]
    print(f"  Layer {layer}  (N={len(zs)}):  <z> = {np.mean(zs):.4f} Å")

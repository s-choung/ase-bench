import numpy as np
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EquationOfState

# 1. Equilibrium lattice constant via EOS
bulk_cu = bulk('Cu', 'fcc', a=3.6)
volumes, energies = [], []

for s in np.linspace(0.95, 1.05, 11):
    atoms = bulk_cu.copy()
    atoms.set_cell(bulk_cu.cell * s, scale_atoms=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, _, _ = eos.fit()
a_eq = v0 ** (1/3)  # FCC: V = a^3
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")

# 2. (111) 4-layer slab
slab = fcc111('Cu', size=(4, 4, 4), a=a_eq, vacuum=10.0)

# 3. Fix bottom 2 layers by z-coordinate
z = slab.get_positions()[:, 2]
z_r = np.round(z, 2)  # Group atoms into layers
layer_zs = np.sort(np.unique(z_r))
mask = np.isin(z_r, layer_zs[:2])
slab.set_constraint(FixAtoms(mask=mask))

# 4. Relaxation
slab.calc = EMT()
BFGS(slab, trajectory='slab_relax.traj').run(fmax=0.05)

# 5. Output
print(f"Final energy: {slab.get_potential_energy():.4f} eV")
z_final = slab.get_positions()[:, 2]
for zval in np.sort(np.unique(np.round(z_final, 3))):
    mask = np.abs(z_final - zval) < 0.05
    print(f"Layer average z: {z_final[mask].mean():.4f} Å")

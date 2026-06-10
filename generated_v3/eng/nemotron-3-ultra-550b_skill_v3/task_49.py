import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111, add_vacuum
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.constraints import FixAtoms

# 1. Find equilibrium lattice constant via EOS
a0_guess = 3.6
volumes, energies = [], []
for x in np.linspace(0.95, 1.05, 9):
    a = a0_guess * x
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)
print(f"Equilibrium lattice constant: {a_eq:.4f} Å")

# 2. Create (111) 4-layer slab with equilibrium lattice constant
slab = fcc111('Cu', size=(1, 1, 4), a=a_eq, vacuum=10.0)

# 3. Attach EMT calculator
slab.calc = EMT()

# 4. Fix bottom 2 layers (tags 3 and 4 for 4-layer slab)
# fcc111 assigns tags: layer 1 (top) = 1, layer 2 = 2, layer 3 = 3, layer 4 (bottom) = 4
mask = [atom.tag >= 3 for atom in slab]
slab.set_constraint(FixAtoms(mask=mask))

# 5. Run BFGS surface relaxation
opt = BFGS(slab, trajectory='relax.traj')
opt.run(fmax=0.01)

# 6. Print final energy and average z per layer
print(f"\nFinal energy: {slab.get_potential_energy():.6f} eV")

# Group atoms by layer (tag)
for tag in sorted(set(atom.tag for atom in slab)):
    z_vals = [atom.position[2] for atom in slab if atom.tag == tag]
    avg_z = np.mean(z_vals)
    print(f"Layer {tag}: average z = {avg_z:.4f} Å")

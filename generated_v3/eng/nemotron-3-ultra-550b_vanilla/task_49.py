from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.optimize import BFGS
from ase.constraints import FixAtoms
import numpy as np

# 1. Bulk EOS for Cu FCC
volumes, energies = [], []
for a in np.linspace(3.4, 3.8, 7):
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a0 = v0 ** (1/3)
print(f"Equilibrium lattice constant: {a0:.4f} Å")

# 2. Create (111) 4-layer slab (2x2 surface cell)
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=15.0)
slab.calc = EMT()

# 3. Fix bottom 2 layers
n_per_layer = len(slab) // 4
fix_indices = list(range(2 * n_per_layer))
slab.set_constraint(FixAtoms(indices=fix_indices))

# 4. BFGS relaxation
opt = BFGS(slab, trajectory='slab.traj', logfile='slab.log')
opt.run(fmax=0.01)

# 5. Print final energy and average z per layer
final_energy = slab.get_potential_energy()
print(f"Final energy: {final_energy:.6f} eV")

pos = slab.get_positions()
for i in range(4):
    layer_indices = slice(i * n_per_layer, (i + 1) * n_per_layer)
    avg_z = pos[layer_indices, 2].mean()
    print(f"Layer {i+1}: average z = {avg_z:.4f} Å")

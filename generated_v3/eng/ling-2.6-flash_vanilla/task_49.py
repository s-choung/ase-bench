from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import BFGS
from ase.eos import EOS
import numpy as np

# 1. Find equilibrium lattice constant for Cu FCC bulk using EOS
cuboid = Atoms('Cu', cell=[[1,0,0],[0,1,0],[0,0,1]]*3.6, pbc=True)
cuboid.calc = EMT()
eos = EOS(cuboid)
volumes, energies = [], []
for v in np.linspace(0.9, 1.1, 7) * cuboid.get_volume():
    cu = cuboid.copy()
    cu.set_volume(v, fixdensity=True)
    cu.get_potential_energy()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())
params = eos.fit(volumes, energies)
a_eq = params[1]**(1/3) * 2  # a = 2 * cube root of volume per atom for 4-atom FCC cell

# 2. Create (111) 4-layer slab with equilibrium lattice constant
slab = Atoms('Cu4',
             cell=[[a_eq/2, -a_eq/2, 0],
                   [a_eq/2,  a_eq/2, 0],
                   [a_eq/2, a_eq/2, a_eq/2]] * 2,
             pbc=[True, True, False])
slab.center(axis=2, vacuum=10.0)
slab = slab.repeat((2, 2, 1))  # Create sufficient surface area

# Select and fix bottom 2 layers
bottom = slab.positions[:,2] < slab.positions[:,2].mean() - a_eq/4
FixAtoms(indices=[i for i, atom in enumerate(slab) if bottom[i]]).apply(slab)

# 3. Attach EMT and run BFGS relaxation
slab.calc = EMT()
dyn = BFGS(slab)
dyn.run(fmax=0.05)

# 4. Print final energy
print(f"Final energy: {slab.get_potential_energy():.4f} eV")

# 5. Print average z-coordinate for each layer
positions = slab.positions
indices_by_layer = []
z_sorted = sorted(range(len(positions)), key=lambda i: positions[i, 2])
n_atoms_per_layer = len(slab) // 4  # 4-layer slab
for layer in range(4):
    start = layer * n_atoms_per_layer
    layer_indices = z_sorted[start:start + n_atoms_per_layer]
    avg_z = np.mean(positions[layer_indices, 2])
    print(f"Layer {layer+1} avg z: {avg_z:.4f}")

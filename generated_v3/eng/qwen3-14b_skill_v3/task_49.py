import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState

# Step 1: Determine equilibrium lattice constant for Cu FCC using EOS
a_values = np.linspace(3.5, 3.7, 7)
volumes, energies = [], []
for a in a_values:
    atoms = bulk('Cu', 'fcc', a=a, cubic=True)
    atoms.calc = EMT()
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())

eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)

# Step 2: Create (111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), vacuum=10.0, a=a_eq)
slab.calc = EMT()

# Step 3: Fix bottom 2 layers using z-coordinates
positions = slab.get_positions()
z = positions[:, 2]
sorted_indices = np.argsort(z)
num_atoms = len(z)
layer1 = sorted_indices[:num_atoms//4]
layer2 = sorted_indices[num_atoms//4:2*num_atoms//4]
mask = np.zeros(len(slab), dtype=bool)
mask[layer1] = mask[layer2] = True
slab.set_constraint(FixAtoms(mask=mask))

# Step 4: Relax surface
opt = BFGS(slab)
opt.run(fmax=0.05)

# Step 5: Compute and print final energy and layer averages
final_energy = slab.get_potential_energy()
positions = slab.get_positions()
z = positions[:, 2]
sorted_indices = np.argsort(z)
sorted_z = z[sorted_indices]

layer1_z = sorted_z[:len(sorted_z)//4]
layer2_z = sorted_z[len(sorted_z)//4:2*len(sorted_z)//4]
layer3_z = sorted_z[2*len(sorted_z)//4:3*len(sorted_z)//4]
layer4_z = sorted_z[3*len(sorted_z)//4:]

print(f"Final energy: {final_energy} eV")
print(f"Layer 1 avg z: {np.mean(layer1_z):.2f} Å")
print(f"Layer 2 avg z: {np.mean(layer2_z):.2f} Å")
print(f"Layer 3 avg z: {np.mean(layer3_z):.2f} Å")
print(f"Layer 4 avg z: {np.mean(layer4_z):.2f} Å")

import numpy as np
from ase.build import bulk, fcc111, surface
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState
from ase.constraints import FixAtoms

# Find equilibrium lattice constant
a_list = np.linspace(3.4, 3.7, 9)
energies = []
for a in a_list:
    atoms = bulk('Cu', 'fcc', a=a)
    atoms.calc = EMT()
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(a_list, energies, 'sj')
a0, e0, B = eos.fit()
print('Equilibrium lattice constant:', a0)

# Create 4-layer Cu(111) slab
slab = fcc111('Cu', size=(4, 4, 4), a=a0, vacuum=6.0)
slab.calc = EMT()

# Fix bottom 2 layers
mask = slab.positions[:, 2] < np.median(slab.positions[:, 2])
slab.set_constraint(FixAtoms(mask=mask))

# Relax
opt = BFGS(slab, trajectory='slab.traj', logfile='slab.log')
opt.run(fmax=0.02)

# Results
e_final = slab.get_potential_energy()
print('Final energy:', e_final)

# Average z per layer
z = slab.positions[:, 2]
layer_z = []
for i in range(4):
    layer = z[i*16:(i+1)*16]
    layer_z.append(np.mean(layer))
for i, zavg in enumerate(layer_z):
    print(f'Layer {i+1} avg z: {zavg:.6f}')

import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.eos import EquationOfState
from ase.optimize import BFGS

# EOS fitting for Cu bulk
cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_bulk.calc = EMT()
volumes, energies = [], []
cell = cu_bulk.get_cell()
for x in np.linspace(0.95, 1.05, 7):
    atoms = cu_bulk.copy()
    atoms.set_cell(cell * x, scale_atoms=True)
    volumes.append(atoms.get_volume())
    energies.append(atoms.get_potential_energy())
eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
a0, _, _ = eos.fit()

# Create (111) slab with equilibrium lattice constant
slab = fcc111('Cu', size=(2, 2, 4), a=a0, vacuum=10.0)
slab.calc = EMT()
slab.set_constraint(FixAtoms(mask=[a.tag < 2 for a in slab]))  # Fix bottom 2 layers

# BFGS relaxation
opt = BFGS(slab)
opt.run(fmax=0.01)

# Analyze results
energy = slab.get_potential_energy()
z_coords = slab.positions[:, 2]
layer_z = [np.mean(z_coords[i*len(slab)//4:(i+1)*len(slab)//4]) for i in range(4)]

print(f'Final energy: {energy:.4f} eV')
print('Average z-coordinates per layer:', layer_z)

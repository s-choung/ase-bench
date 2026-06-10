#!/usr/bin/env python3
from ase import Atoms, Atom
from ase.cluster import bulk
from ase.cell import scale_cell
from ase.calculators.lj import LJ
from ase.constraints import FixAtoms
from ase.optimizers import BFGS
from ase.eos import EquationOfState
import numpy as np

# ---------- Bulk equilibrium ----------
bulk = bulk('Cu', 'fcc', a=3.6)          # guess lattice constant
lj = LJ()
bulk.set_calculator(lj)

eos = EquationOfState(bulk, ['variable_symmetry'])
energy, volume, a = eos.run()
print(f'Bulk a = {a:.6f} Å')

# ---------- Build 111 FCC slab ----------
center = bulk.center(vacuum=10., axis=2)
slab = scale_cell(center, lattice_constant=a)
# Remove top half of the slab
n = len(slab)
slab = slab[:n//2]

# Fix bottom 2 layers (z = 0, 1)
mask = slab.z >= 0
const = FixAtoms(mask, indices=[0, 1])
slab.constraints = const
slab.set_calculator(lj)

# ---------- Surface relaxation ----------
relaxed = BFGS(slab, trajectory='slab.traj')
relaxed.run(fmax=0.05)

# ---------- Print results ----------
print('\nSlab energy =', relaxed.get_potential_energy())
print('Layer coordinates (z):')
for i in range(len(slab)):
    print(f'  layer {i}: {slab[i].calc.get_positions()[0][2]:.6f} Å')

#!/usr/bin/env python3
# NEB simulation with EMT calculator
from ase import Atoms
from ase.neb import NEB
from ase.calculators.emt import EMT
import numpy as np

# Set periodic boundaries (non‑periodic system)
periodic = False

# Initial state: Al – Al distance 5 Å, rigid Al atoms
init = Atoms('Al2',
            positions=[[0, 0, 0], [5, 0, 0]],
            cell=np.eye(3)*20,
            pbc=periodic)

# Final state: Al – Al distance 8 Å, rigid Al atoms
final = Atoms('Al2',
             positions=[[0, 0, 0], [8, 0, 0]],
             cell=np.eye(3)*20,
             pbc=periodic)

# Calculate energies for initial and final
init.set_calculator(EMT())
init_energy = init.get_potential_energy()
print(f'Init energy = {init_energy:.4f} eV')

final.set_calculator(EMT())
final_energy = final.get_potential_energy()
print(f'Final energy = {final_energy:.4f} eV')

# Create images list: 1 initial + 3 intermediate + 1 final
images = [init]

# Linear spacing between distances
for n in range(1, 4):
    dist = 5 + n*(3)/4   # 5 → 6.75 → 8.5
    pos = [atoms.positions[0], [dist, 0, 0]]
    atoms = Atoms('Al2', positions=pos, cell=np.eye(3)*20, pbc=periodic)
    atoms.calc = EMT()
    images.append(atoms)

images.append(final)

# NEB calculator
neb = NEB(images)
neb.calc = EMT()

# Run the NEB calculation
neb.run()
print('NEB finished')

# Print energy of each image
for i, im in enumerate(images):
    im.calc = EMT()
    print(f'Image {i:1d} (state {im.state:.2f}) energy = {im.get_potential_energy():.4f} eV')

# Optional: print forces to show termination
print('\nForces (eV/Å):')
for i, im in enumerate(images):
    print(f'Image {i:1d} forces = {im.get_forces()}')

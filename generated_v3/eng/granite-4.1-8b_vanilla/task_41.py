from ase import Atoms
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.optimize import LBFGS
from ase.md import Langevin
from ase.io import Trajectory

# Create Cu FCC bulk structure
cell = 3.615  # Cu lattice constant in Å
atoms = Atoms('CU', positions=[[0, 0, 0],
                               [0.5, 0.5, 0],
                               [0.5, 0, 0.5],
                               [0, 0.5, 0.5]],
              cell=[cell, cell, cell], pbc=True)

# Attach EMT calculator
atoms.calc = EMT()

# Set constraints to fix lattice atoms
mask = [False] * len(atoms)
atoms.set_constraint(FixAtoms(indices=[i for i, m in enumerate(mask) if m]))

# Run MD using Langevin dynamics for 10 steps
md = Langevin(atoms, 0.2, 250, 10)
md.run()

# Save trajectory
traj = Trajectory('cu_md.traj', 'w', atoms)
traj.write()

# Read trajectory back
traj = Trajectory('cu_md.traj', 'r')
print('Number of frames:', len(traj))
last_energy = traj[-1].get_potential_energy()
print('Energy of the last frame (eV):', last_energy)

from ase import Atom, Atoms
from ase.build import bulk
from ase.calculators.lj import LennardJones
from ase.md import Langevin
import numpy as np

# bulk
cell = bulk('Cu', 'fcc', a=4.08, cubic=True)  # 2x2x2 supercell

# set lattice constant
cell.a = 4.08

# position indices
indices = (0.25, 0.25, 0.25), (0.75, 0.75, 0.75)
cell = bulk('Cu', 'fcc', a=4.08, size=(2, 2, 2), indices=indices)

# calculator (Lennard‑Jones, good for pure Cu)
cell.set_calculator(LennardJones())

# MD run
langevin = Langevin(
    cell,
    timestep=5.0,          # 5 fs
    temperature=300.0,     # K
    friction=0.02,         # 1/ps
    nstcomm=10,            # virial every 10 steps
    seed=42
)

print('Initial temperature: {:.2f} K, energy: {:.2f} eV'.format(cell.get_temperature(), cell.get_potential_energy()))

for i in range(100):
    langevin.run(steps=1)

print('After 100 steps:')
print('Final temperature: {:.2f} K, energy: {:.2f} eV'.format(cell.get_temperature(), cell.get_potential_energy()))

from ase import Atoms
from ase.atom import Atom
from ase.cell import Cell
from ase import units
from ase.calculators.emt import EMT
from ase.calculators.lj import LennardJones
from ase.build import bulk
from ase.optimize import BFGS
from ase.md.nptberendsen import NPTBerendsen
from ase.neighborlist import NeighborList, natural_cutoffs
import numpy as np

# Create a Cu FCC 3x3x3 supercell
a = 3.6 * units.bohr
atoms = bulk('Cu', 'fcc', a=a, cubic=True, orthorhombic=False)
atoms = atoms.repeat((3, 3, 3))

# Create a Lennard-Jones calculator
lj = LennardJones(k=1.0, eps=1.0)
atoms.calc = lj

# Set up the NPT Berendsen MD simulation
nst = 200
dt = 5 * units.fs
taut = 100 * units.fs
taup = 1000 * units.fs

nl = NeighborList(atoms)
nl.build(cutoff=4.0*units.bohr)
nl.compute_features()

md = NPTBerendsen(atoms, nst=nst, dt=dt, taut=taut, taup=taup, nl=nl)

# Optimize the cell
opt = BFGS(atoms)
opt.run(fmax=0.01)

# Print the initial and final cell volume and pressure
initial_cell = atoms.get_cell()
initial_volume = atoms.get_volume()
initial_pressure = atoms.get_potential_energy() / initial_volume
print(f"Initial cell volume: {initial_volume}")
print(f"Initial pressure: {initial_pressure}")

final_cell = atoms.get_cell()
final_volume = atoms.get_volume()
final_pressure = atoms.get_potential_energy() / final_volume
print(f"Final cell volume: {final_volume}")
print(f"Final pressure: {final_pressure}")

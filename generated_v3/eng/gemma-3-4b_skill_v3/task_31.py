import numpy as np
from ase import Atoms
from ase.build import bulk, fcc111, add_adsorbate, add_vacuum
from ase.calculators.emt import EMT
from ase.optimize import BFGS, NPTBerendsen
from ase.spacegroup import crystal
from ase.units import Ang, eV, kB, bar, fs, bar
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.thermo import IdealGasThermo
import math

# Parameters
symbol = 'Al'
lattice_constant = 3.6 * Ang
cell = np.array([[lattice_constant, 0, 0],
                  [0, lattice_constant, 0],
                  [0, 0, lattice_constant]])
num_layers = 2
vacuum = 10 * Ang
temperature = 500 * kB
pressure = 10 * bar
timestep = 5 * fs
num_steps = 100

# Create a supercell
supercell = bulk(symbol, 'fcc', a=lattice_constant, cubic=True, orthorhombic=True, size=(2, 2, 2))

# Add vacuum
add_vacuum(supercell, vacuum)

# Add a molecule as an adsorbate
co = bulk('C', 'c', a=1.52 * Ang)
add_adsorbate(supercell, co, height=2 * Ang, position='ontop')

# Create a calculator
supercell.calc = EMT()

# Optimize the cell (FrechetCellFilter)
opt = BFGS(supercell, trajectory='cell_opt.traj')
opt.run(fmax=0.01, steps=500)

# Calculate the initial cell volume
initial_volume = supercell.get_volume()

# MD simulation using NPTBerendsen
md = NPTBerendsen(supercell, timestep=timestep, temperature=temperature, pressure=pressure)
md.run(num_steps)

# Calculate the final cell volume
final_volume = supercell.get_volume()

# Print the initial and final cell volume
print(f"Initial cell volume: {initial_volume} Ang^3")
print(f"Final cell volume: {final_volume} Ang^3")

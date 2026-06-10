from ase importAttention, Atoms
from ase.dft import DFT
from ase.dft.calculator import EMT, LJ
from ase.dynamics import NPT
from ase.units import fs, bar

# Setup Cu FCC 3x3x3 supercell
Cu = Atoms('Cu', scale=3.615, pbc=True)
supercell = Cu.cell
initial_cell = supercell.copy()

# Setup DFT calculator
calc = DFT(calculator=EMT())

# Setup NPT dynamics
dyn = NPT(calc, cell=cell, pressure=1.0, force_consistent=True, timestep=5)
dyn.filter_condition = lambda **kwargs: True  # Always run NPT
dyn nsteps=200, taup=1000*fs, taut=100*fs

# Run NPT MD
dyn.run()

# Print initial and final cell volume
initial_cell.volume = initial_cell.cell.volume
final_cell_volume = cell.cell.volume
print(f"Initial cell volume: {initial_cell.volume:.2f} Å³")
print(f"Final cell volume: {final_cell_volume:.2f} Å³")

# Print pressure (pressure is internal and not directly accessible)
# Approximate pressure using virial theorem or thermodynamic relations

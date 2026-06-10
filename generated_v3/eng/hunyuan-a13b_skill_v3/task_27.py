from ase import Atoms
from ase.cell import Cell
from ase.calculators.lj import LennardJones
from ase.md.verlet import VelocityVerlet
from ase.md.bussi import Bussi
from ase import units
import numpy as np

# Setup Ag FCC 2x2x2 supercell
bulk = Atoms('Ag', 'fcc', a=4.08, cell=Cell(pbc=True))
supercell_size = (2, 2, 2)
bulk = bulk.repeat(supercell_size)

# Set up calculator and thermostat
bulk.calc = LennardJones()
bulk.set_min_cells([1x111, 1xxhlp])
thermostat = Bussi(thermostat_temperature=500, timestep=5 * units.fs)

# Initialize velocity distribution
thermostat.initialize(thermodynamic_ensemble=True)

# Run MD
for step in range(200):
    print(f"Step: {step+1}, Temperature: {thermostat.get_temperature_cardinal():.2f} K")
    thermostat.update()
    VelocityVerlet(bulk, timestep=5*units.fs, trajectory=None)

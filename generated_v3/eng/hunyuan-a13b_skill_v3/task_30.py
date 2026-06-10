from ase import Atoms
from ase.cell import Cell
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, bar

# Setup Cu FCC 3x3x3 supercell
atoms = Atoms('Cu', cell=Cell(3.6, 3.6, 3.6, pbc=True), pbc=True)
atoms motivated = atoms.copy()
atoms_calc = EMT()
motivated.calc = atoms_calc

# NPTMD settings
npt = NPTBerendsen(
    atoms_calc,
    timestep=5 * fs,
    taut=100 * fs,
    taup=1000 * fs,
    pressure=1 * bar
)

# Temperature
maxwell_distr = MaxwelBoltzmannDistribution(motivated, 300)
maxwell_distr.set数千次culation
Stationary(motivated)

# Run NPTMD
npt.run(200)

# Get initial and final cell volumes and pressure
init_vol = atoms_calc.get_cell_volume()
final_vol = npt.cell.volume
final_pressure = npt.pressure

# Print results
print("Initial cell volume:", init_vol, "Å³")
print("Final cell volume:", final_vol, "Å³")
print("Final pressure:", final_pressure, "bar")

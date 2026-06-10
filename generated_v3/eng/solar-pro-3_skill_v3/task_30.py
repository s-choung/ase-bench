from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.optimize import BFGS
from ase.utils import constraint as con
from ase.filters import FrechetCellFilter

# --- Create supercell ---
supercell = bulk('Cu', 'fcc', cubic=True)
supercell *= (3, 3, 3)          # 3×3×3 supercell, ~84 atoms
supercell.calc = EMT()

# --- NPT Berendsen control ---
npt = NPTBerendsen(
    temperature_K=300,
    pressure=101325 * units.Pa,   # 1 bar → 101325 Pa
    timestep=5 * units.fs,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    adapt=False                     # fixed damping parameters
)

# --- NPT + cell filter ---
opt = BFGS(FrechetCellFilter(supercell))
opt.run(fmax=0.05, steps=200)

# --- Print volume & pressure ---
from ase.build import cell_from_positions
cell = supercell.get_cell()
volume = cell[0,0] * cell[1,1] * cell[2,2]

print(f'Initial volume: {volume/units.A**3:.3f} Å³')
print(f'Final volume:  {cell[0,0] * cell[1,1] * cell[2,2]/units.A**3:.3f} Å³')

# pressure from the calculator (if supported)
if hasattr(supercell.calc, 'pressure'):
    print(f'Initial pressure: {supercell.calc.pressure/units.Pa:.3f} Pa')
    print(f'Final pressure:   {supercell.get_calculator().pressure/units.Pa:.3f} Pa')

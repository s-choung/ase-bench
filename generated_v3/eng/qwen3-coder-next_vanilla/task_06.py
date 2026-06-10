from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create Cu FCC 2x2x2 supercell
cu = bulk('Cu', 'fcc', a=3.61)
supercell = cu.repeat((2, 2, 2))

# Set up EMT calculator
supercell.calc = EMT()

# Equilibrate briefly to get reasonable starting structure
from ase.optimize import BFGS
BFGS(supercell).run(fmax=0.05)

# Get initial energy and temperature
initial_energy = supercell.get_total_energy()
initial_temperature = supercell.get_temperature()

# Set up Langevin dynamics at 300K
dyn = Langevin(
    supercell,
    timestep=5.0 * units.fs,
    temperature=300 * units.kB,
    friction=0.1 / units.fs
)

# Run 100 steps
dyn.run(100)

# Get final temperature and energy
final_energy = supercell.get_total_energy()
final_temperature = supercell.get_temperature()

# Print results
print(f"Initial temperature: {initial_temperature:.2f} K")
print(f"Initial energy: {initial_energy:.6f} eV")
print(f"Final temperature: {final_temperature:.2f} K")
print(f"Final energy: {final_energy:.6f} eV")

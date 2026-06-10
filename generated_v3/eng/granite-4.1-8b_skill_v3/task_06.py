from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.md.langevin import Langevin
from ase import units

# Create a 2x2x2 supercell of FCC Cu
bulk_cell = bulk('Cu', 'fcc', a=3.615)
supercell = bulk_cell.repeat((2, 2, 2))

# Set EMT calculator
supercell.calc = EMT()

# Optimize geometry to get a reasonable starting point
optimizer = BFGS(supercell)
optimizer.run(fmax=0.01)

# Langevin MD parameters
temperature = 300  # K
timestep = 5 * units.fs

# Set initial velocities for Maxwell-Boltzmann distribution
MaxwellBoltzmannDistribution(supercell, temperature=temperature)

# Apply constraint to freeze cell (optional, but common for MD)
# supcell.set_constraint(FixAtoms(mask=[atom.tag >= 3 for atom in supercell]))

# Run Langevin MD
md = Langevin(supercell, timestep=timestep, temperature=temperature, friction=0.01 / units.fs)
md.run(steps=100)

# Print initial and final temperature and total energy
initial_energy = supcell.get_potential_energy()  # After optimization
final_energy = supercell.get_potential_energy()  # After MD
initial_temp = None
final_temp = md.get_temperature()

print(f"Initial energy (after optimization): {initial_energy:.3f} eV")
print(f"Final energy (after MD): {final_energy:.3f} eV")
print(f"Initial temperature: {initial_temp:.2f} K")
print(f"Final temperature: {final_temp:.2f} K")

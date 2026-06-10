from ase.build import bulk
from ase.md.langevin import Langevin
from ase import units

# Setup system: Cu FCC 2x2x2 supercell
atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms = atoms * (2, 2, 2)

# Using LJ potential as a placeholder (ASE built-in)
# Real Cu would require EAM, but instruction specifies built-in calculators
from ase.calculators.lj import LJ
atoms.calc = LJ(sigma=2.3, epsilon=0.01)

# Initialize MD
T_target = 300 # Kelvin
timestep = 5 * units.fs
steps = 100

def print_stats(phase):
    # Langevin uses temperature in Kelvin internally via units.kB
    # The atoms.get_total_energy() returns energy in eV
    # We estimate temperature from kinetic energy: E_kin = 3/2 * N * kB * T
    # However, for simplicity in a script, we access the MD object's temperature
    print(f"{phase} Temperature: {md.get_temperature():.2f} K")
    print(f"{phase} Total Energy: {atoms.get_total_energy():.4f} eV")

# Langevin thermostat
md = Langevin(atoms, timestep, temperature_K=T_target, friction=0.01)

print("Starting MD...")
print_stats("Initial")

# Run MD
for _ in range(steps):
    md.run(1)

print("MD Finished.")
print_stats("Final")

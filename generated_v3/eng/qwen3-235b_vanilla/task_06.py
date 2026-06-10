from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units

# Create Cu FCC 2x2x2 supercell
cu = bulk('Cu', 'fcc') * (2, 2, 2)
cu.calc = EMT()

# Initialize velocities for 300K
cu.set_temperature(300)

# Print initial temperature and energy
print(f"Initial temperature: {cu.get_temperature():.2f} K")
print(f"Initial energy: {cu.get_potential_energy() + cu.get_kinetic_energy():.3f} eV")

# Setup Langevin dynamics
dyn = Langevin(cu, timestep=5 * units.fs, temperature_K=300, friction=0.005)

# Run MD for 100 steps
def print_energy(atoms):
    epot = atoms.get_potential_energy()
    ekin = atoms.get_kinetic_energy()
    print(f"T = {atoms.get_temperature():.2f} K, E = {epot + ekin:.3f} eV")

dyn.attach(print_energy, interval=50)
dyn.run(100)

# Print final temperature and energy
print(f"Final temperature: {cu.get_temperature():.2f} K")
print(f"Final energy: {cu.get_potential_energy() + cu.get_kinetic_energy():.3f} eV")

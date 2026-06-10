from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.velocity_verlet import VelocityVerlet
from ase import units

# Create Pd FCC 2x2x2 supercell
lattice_parameter = 3.89
unit_cell = Atoms('Pd',
                  cell=[lattice_parameter] * 3,
                  pbc=True)
atoms = unit_cell.repeat((2, 2, 2))

# Set up calculator and initial temperature
atoms.calc = EMT()
atoms.set_temperature(500 * units.kB)  # 500K in eV

# Calculate initial total energy
e_initial = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Setup Velocity Verlet MD
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(steps=200)

# Calculate final total energy
e_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()

# Output results
print(f"Initial total energy: {e_initial:.6f} eV")
print(f"Final total energy:   {e_final:.6f} eV")
print(f"Energy difference:    {e_final - e_initial:.6f} eV")

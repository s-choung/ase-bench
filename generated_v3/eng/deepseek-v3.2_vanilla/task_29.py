from ase import Atoms
from ase.md.verlet import VelocityVerlet
from ase.md import MDLogger
from ase.calculators.emt import EMT
from ase import units
import numpy as np

# Create FCC Pd 2x2x2 supercell
atoms = Atoms('Pd4', positions=[[0, 0, 0]], cell=[2.0, 2.0, 2.0], pbc=True)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

# Set initial temperature
atoms.set_momenta(np.random.randn(len(atoms), 3) * np.sqrt(500 * units.kB))

# Initialize MD
dyn = VelocityVerlet(atoms, 2 * units.fs)
initial_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()

# Run MD
def print_energy(a):
    e_kin = a.get_kinetic_energy()
    e_pot = a.get_total_energy()
    print(f"Step {dyn.get_number_of_steps():3d}: E_tot = {e_kin + e_pot:.4f} eV")

dyn.attach(print_energy, interval=200)
dyn.run(200)

# Calculate energy difference
final_energy = atoms.get_total_energy() + atoms.get_kinetic_energy()
energy_diff = final_energy - initial_energy
print(f"\nEnergy difference: {energy_diff:.6e} eV")

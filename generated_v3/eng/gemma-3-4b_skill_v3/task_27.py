import numpy as np
from ase import Atoms
from ase.calculators.emt import EMT
from ase.build import bulk, fcc111
from ase.md.langevin import Langevin
from ase.thermochemistry import IdealGasThermo
from ase.visualize import view

# Create an Ag FCC supercell
atoms = bulk('Ag', 'fcc', a=3.61, cubic=True, orthorhombic=True).repeat((2, 2, 2))
atoms.calc = EMT()

# Set up the Langevin thermostat
temperature = 500.0
friction = 0.01 / units.fs
langevin = Langevin(atoms, timestep=5 * units.fs, temperature_K=temperature, friction=friction)

# Run the MD simulation
num_steps = 200
for i in range(num_steps):
    langevin.run(1)
    if (i + 1) % 50 == 0:
        temp = atoms.get_temperature()
        print(f"Step {i + 1}: Temperature = {temp:.2f} K")

# Get the Gibbs free energy at 298.15 K and 101325 Pa
vib_energies = atoms.vib_energies
thermo = IdealGasThermo(vib_energies=vib_energies, atoms=atoms,
                        geometry='linear', symmetrynumber=2, spin=0)
G = thermo.get_gibbs_energy(temperature=298.15, pressure=101325)
print(f"Gibbs free energy at 298.15 K and 101325 Pa: {G:.4f} eV")

# Visualize the final structure (optional)
# view(atoms)

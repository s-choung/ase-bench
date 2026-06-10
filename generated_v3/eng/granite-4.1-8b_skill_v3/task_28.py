from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase import units
from ase.thermochemistry import IdealGasThermo

# Create a Cu FCC bulk structure
cell = 3.615 * units.angstrom ** 2  # lattice constant of Cu (fcc)
atoms = bulk('Cu', 'fcc', a=cell)
# Create a 2x2x2 supercell
atoms = atoms.repeat((2, 2, 2))

# Set EMT calculator
atoms.calc = EMT()

# Relax the supercell to get a good starting geometry
opt = BFGS(atoms)
opt.run(fmax=0.05)

# Initialize Langevin MD with initial temperature 300 K
t_initial = 300.0  # K
t_final = 600.0    # K
timestep = 5 * units.fs
langevin_md = Langevin(atoms, timestep=timestep, temperature=t_initial, friction=0.01 / units.s)

# Ramp temperature from 300 K to 600 K over 200 steps
temperature_step = (t_final - t_initial) / (200 / 50)
for step in range(1, 201):
    # Update the temperature at every 50 steps
    if step % 50 == 1:
        langevin_md.temperature = t_initial + (step // 50 - 1) * temperature_step
    # Run MD for a single timestep
    langevin_md.run(1)

    # Print the current temperature every 50 steps
    if step % 50 == 0:
        # Get the instantaneous temperature using IdealGasThermo
        thermo = IdealGasThermo(atoms, vibrational_energies=langevin_md.get_vibrational_energies(), geometry='linear', symmetrynumber=2, spin=0)
        current_temp = thermo.get_enthalpy(temperature=langevin_md.temperature) / (atoms.numbers * units.kB)  # approximate
        print(f"Step {step:3d}, Temperature: {langevin_md.temperature:.2f} K")

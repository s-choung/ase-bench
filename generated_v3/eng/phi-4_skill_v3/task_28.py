from ase import Atoms
from ase.build import bulk, make_supercell
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

# Create a Cu FCC bulk structure
atoms = bulk('Cu', 'fcc', a=3.6)
# Create a 2x2x2 supercell
atoms = make_supercell(atoms, [[2, 0, 0], [0, 2, 0], [0, 0, 2]])

# Set the calculator
atoms.calc = EMT()

# Set initial velocities according to Maxwell-Boltzmann distribution at 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

# Langevin dynamics setup
dyn = Langevin(atoms, timestep=5 * units.fs, temperature_K=300, friction=0.02 / units.fs)

# Run MD with temperature ramp from 300K to 600K over 200 steps
for step in range(200):
    if step % 50 == 0:
        print(f"Step {step}: Temperature = {atoms.get_temperature():.2f} K")
    
    # Update temperature linearly from 300K to 600K
    current_temperature = 300 + (step / 200) * (600 - 300)
    dyn.set_temperature(current_temperature)
    
    dyn.run(1)

from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.io import write
from ase import units

# Create Ag FCC 2x2x2 supercell
atoms = bulk('Ag', crystalstructure='fcc', a=4.09) * (2, 2, 2)
atoms.calc = EMT()

# Set up MD
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)  # Correct COM drift
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=500, friction=0.1)

# Run MD
steps = 200
print("Temperature every 50 steps:")
for i in range(steps // 50):
    dyn.run(50)
    temp = atoms.get_temperature()
    print(f"Step {i*50}: Temperature = {temp:.2f} K")

write('ag_md_trajectory.xyz', atoms)

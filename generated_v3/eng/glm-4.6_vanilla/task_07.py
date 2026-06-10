from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.units import fs

# Create Cu FCC bulk
atoms = bulk('Cu', 'fcc', cubic=True)
atoms.calc = EMT()

# Set initial temperature to 300K
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print Initial Energy
e_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial Total Energy: {e_init:.6f} eV")

# Run NVE MD for 50 steps
dyn = VelocityVerlet(atoms, timestep=5 * fs)
dyn.run(50)

# Print Final Energy
e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final Total Energy:   {e_final:.6f} eV")

from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet

# Create Cu FCC bulk
atoms = Atoms('Cu', pbc=True)
atoms *= (3,3,3)
atoms.rattle(0.02 * units.Ang)

# Setup EMT calculator
atoms.calc = EMT()
e0 = atoms.get_potential_energy()

# Initialize and assign temperature
MaxwellBoltzmannDistribution(atoms, 300)
Stationary(atoms)

# Run VelocityVerlet NVE MD
dyn = VelocityVerlet(atoms, timestep=1*units.fs)
print(f"E_initial: {atoms.get_kinetic_energy() + e0:.3f} eV")
dyn.run(50)

# Final stats
e_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"E_final: {e_final:.3f} eV")

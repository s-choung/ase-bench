from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.langevin import Langevin
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Build 2x2x2 FCC Cu supercell
atoms = bulk('Cu', 'fcc', a=3.6).repeat((2, 2, 2))
atoms.calc = EMT()

# Initialize velocities and remove center-of-mass drift
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

# Print initial state
init_temp = atoms.get_temperature()
init_pe = atoms.get_potential_energy()
print(f"Initial | T: {init_temp:.1f} K, PE: {init_pe:.3f} eV")

# Run Langevin NVT MD
dyn = Langevin(atoms, timestep=5*units.fs, temperature_K=300, friction=0.01/units.fs)
dyn.run(100)

# Print final state
final_temp = atoms.get_temperature()
final_pe = atoms.get_potential_energy()
print(f"Final   | T: {final_temp:.1f} K, PE: {final_pe:.3f} eV")

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

# Build Pd FCC 2x2x2 supercell and attach EMT calculator
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initialize velocities at 500 K and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Record initial total energy (potential + kinetic)
E0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

# NVE MD with VelocityVerlet, 2 fs timestep, 200 steps
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# Record final total energy and print energy drift
E1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy = {E0:.6f} eV")
print(f"Final total energy   = {E1:.6f} eV")
print(f"ΔE (final‑initial)   = {E1 - E0:.6e} eV")

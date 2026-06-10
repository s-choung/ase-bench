from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

# Setup Pd FCC 2x2x2 supercell
atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

# Initial conditions: 500K and remove COM drift
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

# Energy before MD
e_start = atoms.get_total_energy()

# Run NVE MD
dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

# Energy after MD
e_end = atoms.get_total_energy()

print(f"Energy difference: {abs(e_end - e_start):.6f} eV")

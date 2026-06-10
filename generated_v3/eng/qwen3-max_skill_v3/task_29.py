from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

initial_total_energy = atoms.get_total_energy()

md = VelocityVerlet(atoms, timestep=2 * units.fs)
md.run(200)

final_total_energy = atoms.get_total_energy()
print(f"Energy drift: {final_total_energy - initial_total_energy:.6e} eV")

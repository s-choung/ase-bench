from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=5 * units.fs)

epot = atoms.get_potential_energy()
ekin = atoms.get_kinetic_energy()
print(f'Initial Etot: {epot + ekin:.6f} eV')

dyn.run(50)

epot = atoms.get_potential_energy()
ekin = atoms.get_kinetic_energy()
print(f'Final Etot:   {epot + ekin:.6f} eV')

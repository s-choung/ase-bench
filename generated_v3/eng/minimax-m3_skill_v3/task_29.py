from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc', a=3.89) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e0 = atoms.get_potential_energy() + atoms.get_kinetic_energy()

md = VelocityVerlet(atoms, timestep=2 * units.fs)
md.run(200)

e1 = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"E_start = {e0:.6f} eV")
print(f"E_end   = {e1:.6f} eV")
print(f"|dE|    = {abs(e1 - e0):.2e} eV")

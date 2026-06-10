from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

E_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()

md = VelocityVerlet(atoms, timestep=5 * units.fs)
md.run(50)

E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()

print(f"Initial total energy: {E_init:.6f} eV")
print(f"Final total energy:   {E_final:.6f} eV")
print(f"Energy drift:         {abs(E_final - E_init):.6e} eV")

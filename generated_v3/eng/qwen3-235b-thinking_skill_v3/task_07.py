from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc')
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
E_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn = VelocityVerlet(atoms, timestep=1*units.fs)
dyn.run(50)
E_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"{E_init:.6f} {E_final:.6f}")

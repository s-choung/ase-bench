from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)

dyn = VelocityVerlet(atoms, timestep=5*units.fs)

e_init = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial energy: {e_init:.6f} eV")

dyn.run(50)

e_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final energy: {e_final:.6f} eV")

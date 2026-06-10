from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.velocityverlet import VelocityVerlet
from ase import units

atoms = bulk('Cu', cubic=True) * (3, 3, 3)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300.0)

e_tot_initial = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Initial total energy: {e_tot_initial:.6f} eV")

dyn = VelocityVerlet(atoms, timestep=5.0 * units.fs)
dyn.run(50)

e_tot_final = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f"Final total energy:   {e_tot_final:.6f} eV")

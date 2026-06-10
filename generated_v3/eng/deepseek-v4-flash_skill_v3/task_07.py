from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

E_kin_initial = atoms.get_kinetic_energy()
E_pot_initial = atoms.get_potential_energy()
E_total_initial = E_kin_initial + E_pot_initial

dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.run(50)

E_kin_final = atoms.get_kinetic_energy()
E_pot_final = atoms.get_potential_energy()
E_total_final = E_kin_final + E_pot_final

print(f"Initial total energy: {E_total_initial:.6f} eV")
print(f"Final total energy:   {E_total_final:.6f} eV")
print(f"Energy change:        {E_total_final - E_total_initial:.6f} eV")

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

velverlet = VelocityVerlet(atoms, timestep=5*units.fs)

e_pot_initial = atoms.get_potential_energy()
e_kin_initial = atoms.get_kinetic_energy()
e_tot_initial = e_pot_initial + e_kin_initial
print(f"Initial total energy: {e_tot_initial:.6f} eV")

velverlet.run(50)

e_pot_final = atoms.get_potential_energy()
e_kin_final = atoms.get_kinetic_energy()
e_tot_final = e_pot_final + e_kin_final
print(f"Final total energy:   {e_tot_final:.6f} eV")
print(f"Energy drift:         {e_tot_final - e_tot_initial:.6f} eV")

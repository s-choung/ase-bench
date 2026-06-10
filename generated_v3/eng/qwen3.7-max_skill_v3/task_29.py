from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

e_kin_0 = atoms.get_kinetic_energy()
e_pot_0 = atoms.get_potential_energy()
e_tot_0 = e_kin_0 + e_pot_0

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e_kin_f = atoms.get_kinetic_energy()
e_pot_f = atoms.get_potential_energy()
e_tot_f = e_kin_f + e_pot_f

print(f"Initial total energy: {e_tot_0:.6f} eV")
print(f"Final   total energy: {e_tot_f:.6f} eV")
print(f"Difference          : {e_tot_f - e_tot_0:.6f} eV")

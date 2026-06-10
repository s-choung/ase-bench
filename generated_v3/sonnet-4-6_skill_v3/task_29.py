from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
ZeroRotation(atoms)

e_kin_0 = atoms.get_kinetic_energy()
e_pot_0 = atoms.get_potential_energy()
e_tot_0 = e_kin_0 + e_pot_0
print(f"Initial:  E_kin={e_kin_0:.4f} eV  E_pot={e_pot_0:.4f} eV  E_tot={e_tot_0:.4f} eV")

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e_kin_1 = atoms.get_kinetic_energy()
e_pot_1 = atoms.get_potential_energy()
e_tot_1 = e_kin_1 + e_pot_1
print(f"Final:    E_kin={e_kin_1:.4f} eV  E_pot={e_pot_1:.4f} eV  E_tot={e_tot_1:.4f} eV")
print(f"ΔE_tot = {e_tot_1 - e_tot_0:.6f} eV  ({(e_tot_1 - e_tot_0)/abs(e_tot_0)*100:.4f}%)")

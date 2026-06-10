from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

e_pot = atoms.get_potential_energy()
e_kin = atoms.get_kinetic_energy()
e_tot_initial = e_pot + e_kin
print(f"Initial: E_pot={e_pot:.4f} eV, E_kin={e_kin:.4f} eV, E_tot={e_tot_initial:.4f} eV")

dyn = VelocityVerlet(atoms, timestep=1.0 * units.fs)
dyn.run(50)

e_pot = atoms.get_potential_energy()
e_kin = atoms.get_kinetic_energy()
e_tot_final = e_pot + e_kin
print(f"Final:   E_pot={e_pot:.4f} eV, E_kin={e_kin:.4f} eV, E_tot={e_tot_final:.4f} eV")
print(f"ΔE_tot = {e_tot_final - e_tot_initial:.6f} eV")

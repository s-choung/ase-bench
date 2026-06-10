from ase.build import bulk
from ase.calculators.emt import EMT
from ase import units
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

e_kin_i = atoms.get_kinetic_energy()
e_pot_i = atoms.get_potential_energy()
print(f"Initial Total Energy: {e_kin_i + e_pot_i:.6f} eV (Kinetic: {e_kin_i:.6f} eV, Potential: {e_pot_i:.6f} eV)")

dyn = VelocityVerlet(atoms, timestep=5 * units.fs)
dyn.run(50)

e_kin_f = atoms.get_kinetic_energy()
e_pot_f = atoms.get_potential_energy()
print(f"Final Total Energy: {e_kin_f + e_pot_f:.6f} eV (Kinetic: {e_kin_f:.6f} eV, Potential: {e_pot_f:.6f} eV)")

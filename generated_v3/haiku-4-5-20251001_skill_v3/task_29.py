from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89)
atoms = atoms.repeat((2, 2, 2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

E_initial = atoms.get_total_energy()
KE_initial = atoms.get_kinetic_energy()
print(f"Initial: E_pot={atoms.get_potential_energy():.6f} eV, KE={KE_initial:.6f} eV, E_total={E_initial:.6f} eV")

md = VelocityVerlet(atoms, timestep=2*units.fs)
md.run(200)

E_final = atoms.get_total_energy()
KE_final = atoms.get_kinetic_energy()
print(f"Final:   E_pot={atoms.get_potential_energy():.6f} eV, KE={KE_final:.6f} eV, E_total={E_final:.6f} eV")
print(f"\nEnergy conservation: ΔE_total = {E_final - E_initial:.6f} eV ({abs(E_final - E_initial)/abs(E_initial)*100:.4f}%)")

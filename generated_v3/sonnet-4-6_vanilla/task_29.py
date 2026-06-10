from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units

atoms = bulk('Pd', 'fcc', a=3.89).repeat([2, 2, 2])
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

e_total_initial = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Initial total energy: {e_total_initial:.6f} eV")

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)
dyn.run(200)

e_total_final = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f"Final total energy:   {e_total_final:.6f} eV")
print(f"Energy difference:    {e_total_final - e_total_initial:.6f} eV")
print(f"Relative drift:       {abs(e_total_final - e_total_initial) / abs(e_total_initial) * 100:.6f} %")

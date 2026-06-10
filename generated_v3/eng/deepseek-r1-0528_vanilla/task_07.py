from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase import units

atoms = Atoms('Cu', positions=[[0, 0, 0]], cell=[3.6, 3.6, 3.6], pbc=True)
atoms = atoms.repeat((4, 4, 4))
atoms.calc = EMT()
atoms.get_thermal_energy()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
dyn = VelocityVerlet(atoms, 5 * units.fs)
initial_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
dyn.run(50)
final_energy = atoms.get_potential_energy() + atoms.get_kinetic_energy()
print(f'Initial total energy: {initial_energy:.4f} eV')
print(f'Final total energy: {final_energy:.4f} eV')

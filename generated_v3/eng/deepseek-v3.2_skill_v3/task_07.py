from ase import Atoms
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = Atoms('Cu4', 
              positions=[(0,0,0), (0.5,0.5,0), (0.5,0,0.5), (0,0.5,0.5)], 
              cell=[(2.55,0,0), (0,2.55,0), (0,0,2.55)], 
              pbc=True)

atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

initial_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f'Initial total energy: {initial_energy:.6f} eV')

dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)

final_energy = atoms.get_kinetic_energy() + atoms.get_potential_energy()
print(f'Final total energy:   {final_energy:.6f} eV')
print(f'Energy difference:    {final_energy-initial_energy:.6e} eV')

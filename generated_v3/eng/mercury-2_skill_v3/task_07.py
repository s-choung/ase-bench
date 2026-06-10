from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def total_energy(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

E0 = total_energy(atoms)
md = VelocityVerlet(atoms, timestep=1 * units.fs)
md.run(50)
E1 = total_energy(atoms)

print(f'Initial total energy: {E0:.6f} eV')
print(f'Final total energy:   {E1:.6f} eV')

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def get_total_energy(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

print("Initial total energy: %.6f eV" % get_total_energy(atoms))

dyn = VelocityVerlet(atoms, timestep=5*units.fs)
dyn.run(50)

print("Final total energy:   %.6f eV" % get_total_energy(atoms))

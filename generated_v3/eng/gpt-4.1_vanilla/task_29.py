from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.md.verlet import VelocityVerlet
from ase import units

# System setup
atoms = bulk('Pd', 'fcc', a=3.89).repeat((2,2,2))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)

def get_etot(atoms):
    return atoms.get_potential_energy() + atoms.get_kinetic_energy()

etot0 = get_etot(atoms)

dyn = VelocityVerlet(atoms, 2 * units.fs)
for step in range(200):
    dyn.run(1)

etot1 = get_etot(atoms)
print(f'Energy difference after 200 steps: {etot1 - etot0:.6f} eV')

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units
import numpy as np

atoms = bulk('Pd', 'fcc', a=3.89) * (2,2,2)
atoms.calc = EMT()
MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

def get_total_energy(a):
    return a.get_potential_energy() + a.get_kinetic_energy()

dyn = VelocityVerlet(atoms, timestep=2*units.fs)
e0 = get_total_energy(atoms)
for _ in range(200):
    dyn.run(1)
e1 = get_total_energy(atoms)
print('ΔE = %.6f eV' % (e1 - e0))

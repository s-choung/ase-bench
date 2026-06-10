import numpy as np
from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.verlet import VelocityVerlet
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

atoms = bulk('Pd', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = VelocityVerlet(atoms, timestep=2 * units.fs)

def print_energy_conservation(a=atoms):
    epot = a.get_potential_energy()
    ekin = a.get_kinetic_energy()
    etot = epot + ekin
    print(f'Epot: {epot:.5f} eV | Ekin: {ekin:.5f} eV | Etot: {etot:.5f} eV')
    return etot

etot_initial = print_energy_conservation()

dyn.run(200)

etot_final = print_energy_conservation()

print(f'Difference in Total Energy: {etot_final - etot_initial:.5f} eV')

from ase.build import bulk
from ase.units import GPa, kJ, Angstrom
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary

pressure_GPa = 10
pressure_eV_A3 = pressure_GPa * GPa / (kJ / Angstrom**3)

atoms = bulk('Al', 'fcc', a=4.05) * (2, 2, 2)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)

dyn = NPTBerendsen(atoms, timestep=2 * units.fs, temperature_K=500,
                   pressure=pressure_eV_A3, compressibility=1e-5, taut=0.5)

def print_volume(a):
    print('Volume:', a.get_volume())

print('Initial cell volume:')
print_volume(atoms)

dyn.attach(print_volume, interval=10)
dyn.run(100)

print('Final cell volume:')
print_volume(atoms)

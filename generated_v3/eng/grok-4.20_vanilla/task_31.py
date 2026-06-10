from ase.build import bulk
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase import units
import numpy as np

atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = atoms.get_calculator()  # EMT is default for Al

# Convert 10 GPa to eV/Ang^3
p_target = 10 * GPa

MaxwellBoltzmannDistribution(atoms, temperature_K=500.0)

md = NPTBerendsen(atoms, timestep=5.0*units.fs, temperature=500.0,
                  pressure=p_target, taut=100.0*units.fs, taup=1000.0*units.fs,
                  compressibility=1.0/(200.0*GPa))

print('Initial volume:', atoms.get_volume())

md.run(100)

print('Final volume:', atoms.get_volume())

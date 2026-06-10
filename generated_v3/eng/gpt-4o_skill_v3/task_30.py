import numpy as np
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6) * (3, 3, 3)
atoms.calc = EMT()

def print_status(atoms):
    volume = atoms.get_volume()
    pressure = atoms.get_pressure()
    print(f'Volume: {volume:.2f} Å³, Pressure: {pressure:.2f} bar')

print_status(atoms)

dyn = NPTBerendsen(atoms, timestep=5 * units.fs, temperature_K=300, taut=100 * units.fs, 
                   pressure=1.0 * units.bar, taup=1000 * units.fs)

dyn.run(200)
print_status(atoms)

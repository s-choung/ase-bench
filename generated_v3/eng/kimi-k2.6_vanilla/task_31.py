from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, GPa

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

print("Initial volume:", atoms.get_volume())

# 10 GPa converted to ASE internal pressure units (eV/Ang^3)
dyn = NPTBerendsen(atoms, timestep=2.0 * fs, temperature=500,
                   pressure=10.0 * GPa, taut=100 * fs, taup=500 * fs)
dyn.run(100)

print("Final volume:", atoms.get_volume())

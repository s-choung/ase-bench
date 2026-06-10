from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import fs, GPa

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

P_GPa = 10.0
P_eV_A3 = P_GPa * GPa

print(f"Initial volume: {atoms.get_volume():.3f} Ang^3")

dyn = NPTBerendsen(atoms, timestep=1*fs, temperature=500, 
                   pressure=P_eV_A3, taut=100*fs, taup=1000*fs)
dyn.run(100)

print(f"Final volume: {atoms.get_volume():.3f} Ang^3")

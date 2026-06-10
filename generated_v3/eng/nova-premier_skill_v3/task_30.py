from ase import Atoms, units
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk('Cu', 'fcc', a=3.6) * (3,3,3)
atoms.calc = EMT()

print("Initial Volume:", atoms.get_volume(), "Å³")

dyn = NPTBerendsen(
    atoms,
    timestep=5*units.fs,
    temperature_K=300,
    externalstress=101325*units.Pascal,
    ttime=100*units.fs,
    pfactor=1000*units.fs
)
dyn.run(200)

print("Final Volume:", atoms.get_volume(), "Å³")
print("Pressure:", atoms.get_stress(True)/units.GPa, "GPa")

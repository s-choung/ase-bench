from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (3, 3, 3)
atoms.calc = EMT()

dt = 5 * units.fs
P = 1 * units.bar

dyn = NPTBerendsen(atoms, timestep=dt, temperature_K=300, taut=100*units.fs,
                   pressure=P, taup=1000*units.fs, compressibility=1.0)

print(f"Initial: V={atoms.get_volume():.3f} Å³, P={atoms.get_pressure()/units.bar:.3f} bar")

dyn.run(200)

print(f"Final:   V={atoms.get_volume():.3f} Å³, P={atoms.get_pressure()/units.bar:.3f} bar")

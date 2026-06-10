from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Al', 'fcc') * (2, 2, 2)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.4f} A^3")

md = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=500,
    friction=0.005 / units.fs,
    externalpressure=10 * units.GPa,
    taut=100 * units.fs,
    taup=500 * units.fs
)

md.run(100)

print(f"Final volume: {atoms.get_volume():.4f} A^3")

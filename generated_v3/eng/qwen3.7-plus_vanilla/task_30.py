from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Cu', cubic=True) * (3, 3, 3)
atoms.calc = EMT()

print(f"Initial volume: {atoms.get_volume():.2f} Å^3")
print(f"Initial pressure: {-atoms.get_stress()[:3].mean() / units.bar:.2f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs
)

dyn.run(200)

print(f"Final volume: {atoms.get_volume():.2f} Å^3")
print(f"Final pressure: {-atoms.get_stress()[:3].mean() / units.bar:.2f} bar")

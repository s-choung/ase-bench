from ase import units
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen

atoms = bulk('Cu', cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

npt = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)

def get_pressure(at):
    s = at.get_stress(voigt=True)
    return -(s[0] + s[1] + s[2]) / 3.0

print(f"Initial volume: {atoms.get_volume():.4f} Å^3")
print(f"Initial pressure: {get_pressure(atoms)/units.GPa:.6f} GPa")

npt.run(steps=200)

print(f"Final volume: {atoms.get_volume():.4f} Å^3")
print(f"Final pressure: {get_pressure(atoms)/units.GPa:.6f} GPa")

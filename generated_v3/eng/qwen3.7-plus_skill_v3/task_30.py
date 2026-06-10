from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True).repeat((3, 3, 3))
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def get_pressure(a):
    stress = a.get_stress()
    return -(stress[0] + stress[1] + stress[2]) / 3.0 / units.bar

print(f"Initial volume: {atoms.get_volume():.2f} A^3")
print(f"Initial pressure: {get_pressure(atoms):.2f} bar")

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs
)
dyn.run(200)

print(f"Final volume: {atoms.get_volume():.2f} A^3")
print(f"Final pressure: {get_pressure(atoms):.2f} bar")

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

v0 = atoms.get_volume()
p0 = -atoms.get_stress(voigt=False).trace() / 3.0 / units.bar

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    compressibility_au=7.26e-12 / units.Pascal,
)

dyn.run(200)

v1 = atoms.get_volume()
p1 = -atoms.get_stress(voigt=False).trace() / 3.0 / units.bar

print(f"Initial volume: {v0:.6f} A^3")
print(f"Initial pressure: {p0:.6f} bar")
print(f"Final volume: {v1:.6f} A^3")
print(f"Final pressure: {p1:.6f} bar")

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

p0 = atoms.get_stress(voigt=False)
p0_bar = -(p0[0, 0] + p0[1, 1] + p0[2, 2]) / 3 / units.bar
v0 = atoms.get_volume()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)
ZeroRotation(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure_au=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)
dyn.run(200)

p1 = atoms.get_stress(voigt=False)
p1_bar = -(p1[0, 0] + p1[1, 1] + p1[2, 2]) / 3 / units.bar
v1 = atoms.get_volume()

print(f'Initial volume: {v0:.6f} A^3')
print(f'Initial pressure: {p0_bar:.6f} bar')
print(f'Final volume: {v1:.6f} A^3')
print(f'Final pressure: {p1_bar:.6f} bar')

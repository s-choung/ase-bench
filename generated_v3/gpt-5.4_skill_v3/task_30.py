from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

print(f'Initial volume: {atoms.get_volume():.6f} A^3')
print(f'Initial pressure: {-atoms.get_stress(voigt=False).trace() / 3 / units.bar:.6f} bar')

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

print(f'Final volume: {atoms.get_volume():.6f} A^3')
print(f'Final pressure: {-atoms.get_stress(voigt=False).trace() / 3 / units.bar:.6f} bar')

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary, ZeroRotation
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

initial_volume = atoms.get_volume()

MaxwellBoltzmannDistribution(atoms, temperature_K=500)
Stationary(atoms)
ZeroRotation(atoms)

pressure_gpa = 10.0
pressure_ev_a3 = pressure_gpa / 160.21766208

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=500,
    pressure_au=pressure_ev_a3,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=0.01385 / 160.21766208,
)

dyn.run(100)

final_volume = atoms.get_volume()

print(f'Initial volume: {initial_volume:.6f} A^3')
print(f'Final volume: {final_volume:.6f} A^3')

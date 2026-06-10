from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.6, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

vol_i = atoms.get_volume()
p_i = -atoms.get_stress(voigt=True)[:3].mean() / units.bar

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    taut=100 * units.fs,
    pressure=1.0 * units.bar,
    taup=1000 * units.fs,
    compressibility=4.57e-5 / units.bar
)

dyn.run(200)

vol_f = atoms.get_volume()
p_f = -atoms.get_stress(voigt=True)[:3].mean() / units.bar

print(f"Initial: Volume = {vol_i:.2f} Å^3, Pressure = {p_i:.2f} bar")
print(f"Final:   Volume = {vol_f:.2f} Å^3, Pressure = {p_f:.2f} bar")

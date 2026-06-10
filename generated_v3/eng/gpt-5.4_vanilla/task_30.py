from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Cu', 'fcc', a=3.615, cubic=True) * (3, 3, 3)
atoms.calc = EMT()

MaxwellBoltzmannDistribution(atoms, temperature_K=300)
Stationary(atoms)

def pressure_bar(atoms):
    s = atoms.get_stress(voigt=False, include_ideal_gas=True)
    p_eva3 = -s.trace() / 3.0
    return p_eva3 / units.bar

v0 = atoms.get_volume()
p0 = pressure_bar(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=5 * units.fs,
    temperature_K=300,
    pressure=1.0 * units.bar,
    taut=100 * units.fs,
    taup=1000 * units.fs,
)

dyn.run(200)

vf = atoms.get_volume()
pf = pressure_bar(atoms)

print(f"Initial volume: {v0:.6f} A^3")
print(f"Initial pressure: {p0:.6f} bar")
print(f"Final volume: {vf:.6f} A^3")
print(f"Final pressure: {pf:.6f} bar")

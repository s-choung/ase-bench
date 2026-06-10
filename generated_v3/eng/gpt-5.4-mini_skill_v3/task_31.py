from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution, Stationary
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 500
P_gpa = 10.0
P = P_gpa * 1e9 / units.Pascal * units.Pascal / units.eV * units.Angstrom**3
# simpler and correct conversion:
P = P_gpa * 1e9 / (units.eV / units.Angstrom**3)

v0 = atoms.get_volume()

MaxwellBoltzmannDistribution(atoms, temperature_K=T)
Stationary(atoms)

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=T,
    pressure_au=P,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=1.0 / P,
)

dyn.run(100)

v1 = atoms.get_volume()

print(f"Initial volume: {v0:.6f} Å^3")
print(f"Final volume:   {v1:.6f} Å^3")

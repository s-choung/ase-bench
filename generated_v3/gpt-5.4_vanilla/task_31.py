from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.md.velocitydistribution import MaxwellBoltzmannDistribution
from ase.units import fs, kB

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 500.0
P_GPa = 10.0
P_eVA3 = P_GPa / 160.21766208

MaxwellBoltzmannDistribution(atoms, temperature_K=T)

v0 = atoms.get_volume()
print(f"Initial cell volume: {v0:.6f} A^3")

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * fs,
    temperature_K=T,
    pressure_au=P_eVA3,
    taut=100.0 * fs,
    taup=1000.0 * fs,
    compressibility_au=0.0139 / 160.21766208,
)

dyn.run(100)

v1 = atoms.get_volume()
print(f"Final cell volume: {v1:.6f} A^3")

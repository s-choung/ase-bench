from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = bulk('Al', 'fcc', a=4.05, cubic=True) * (2, 2, 2)
atoms.calc = EMT()

T = 500.0
P_GPa = 10.0
P_eVA3 = P_GPa / 160.21766208

print(f"Pressure: {P_GPa} GPa = {P_eVA3:.6f} eV/Ang^3")
print(f"Initial volume: {atoms.get_volume():.6f} Ang^3")

dyn = NPTBerendsen(
    atoms,
    timestep=1.0 * units.fs,
    temperature_K=T,
    pressure_au=P_eVA3,
    taut=100.0 * units.fs,
    taup=1000.0 * units.fs,
    compressibility_au=0.01389372612462577,
)

dyn.run(100)

print(f"Final volume: {atoms.get_volume():.6f} Ang^3")

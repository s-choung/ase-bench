from ase.build import bulk
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase.units import GPa, fs

atoms = bulk('Al', 'fcc', a=4.05).repeat((2, 2, 2))
atoms.calc = EMT()

pressure = 10 * GPa  # 10 GPa in eV/Ang^3
temperature = 500  # K
timestep = 2 * fs

print(f"Initial volume: {atoms.get_volume():.2f} Ang^3")

dyn = NPTBerendsen(
    atoms,
    timestep,
    temperature_K=temperature,
    pressure_au=pressure,
    taut=100 * fs,
    taup=1000 * fs,
)

dyn.run(100)

print(f"Final volume: {atoms.get_volume():.2f} Ang^3")

from ase.build import face_centered_cubic
from ase.calculators.emt import EMT
from ase.md.nptberendsen import NPTBerendsen
from ase import units

atoms = face_centered_cubic('Cu', a=3.61, size=(3, 3, 3))
atoms.set_calculator(EMT())

initial_volume = atoms.get_volume()
initial_stress = atoms.get_stress()
initial_pressure = sum(initial_stress.diagonal()) / 3.0

pressure = 6.241509e-7  # 1 bar in eV/A³

dyn = NPTBerendsen(
    atoms=atoms,
    temperature=300 * units.K,
    pressure=pressure,
    taut=100 * units.fs,
    taup=1000 * units.fs,
    timestep=5 * units.fs,
    steps=200
)

dyn.run(200)

final_volume = atoms.get_volume()
final_stress = atoms.get_stress()
final_pressure = sum(final_stress.diagonal()) / 3.0

print(f"Initial Volume: {initial_volume} Å³, Pressure: {initial_pressure} eV/Å³")
print(f"Final Volume: {final_volume} Å³, Pressure: {final_pressure} eV/Å³")

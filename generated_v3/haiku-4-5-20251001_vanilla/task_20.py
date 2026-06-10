from ase.build import nanotube
from ase.calculators.emt import EMT

cnt = nanotube(6, 6, length=4)
cnt.set_calculator(EMT())

print(f"Number of atoms: {len(cnt)}")
print(f"Cell parameters:\n{cnt.cell}")
print(f"Cell volume: {cnt.get_volume():.2f} Ų")
print(f"Positions shape: {cnt.positions.shape}")

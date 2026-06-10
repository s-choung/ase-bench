from ase.build import nanotube
from ase.calculators.emt import EMT

# Create (6,6) carbon nanotube with length 4
cnt = nanotube(6, 6, length=4)
cnt.calc = EMT()  # Attach required ASE built-in EMT calculator

print(f"Number of atoms: {len(cnt)}")
print("\nSimulation cell (units: Angstrom):")
print(cnt.cell)

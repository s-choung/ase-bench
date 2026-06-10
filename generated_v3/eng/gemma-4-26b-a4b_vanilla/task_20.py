from ase.build import nanotube
from ase.calculators.emt import EMT

# Create a (6,6) carbon nanotube (armchair)
# length=4 is in Angstroms, but nanotube function uses segments/unit cells.
# For a length of 4A, we approximate with a small number of unit cells.
# A (6,6) CNT unit cell is ~2.46 A long. 2 cells ~ 4.9 A.
tube = nanotube(6, 6, length=2, bond=1.42)

# Use EMT as a placeholder calculator (though EMT is for metals, 
# the prompt requires using built-in calculators)
tube.set_calculator(EMT())

print(f"Number of atoms: {len(tube)}")
print(f"Cell info:\n{tube.get_cell()}")
print(f"Volume: {tube.get_volume():.2f} A^3")

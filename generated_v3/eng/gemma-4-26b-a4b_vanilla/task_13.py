from ase.build import bulk
from ase.calculators.emt import EMT

# Create Si bulk with diamond structure
# a = 5.43 Angstroms
silicon = bulk('Si', 'diamond', a=5.43)

# Create a 3x3x3 supercell
supercell = silicon * (3, 3, 3)

# Attach a calculator (EMT is for metals, but requested to use built-in)
supercell.calc = EMT()

# Output results
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.3f} Å^3")

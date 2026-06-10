from ase.build import bulk
from ase.calculators.emt import EMT  # Example calculator, though not used actively here

# Create a diamond structure for Silicon with lattice constant 5.43 Angstrom
si_bulk = bulk('Si', 'diamond', a=5.43)

# Create a 3x3x3 supercell
supercell = si_bulk ** (3, 3, 3)  

# Print the number of atoms and cell volume
print(f"Number of atoms: {len(supercell)}")
print(f"Cell volume: {supercell.get_volume():.2f} Angstrom^3")

# If you want to attach a calculator (like EMT) and compute energies, you could use:
# calculator = EMT()
# supercell.set_calculator(calculator)
# print(f"Energy: {supercell.get_potential_energy():.2f} eV")

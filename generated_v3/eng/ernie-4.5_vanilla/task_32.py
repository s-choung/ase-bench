from ase import Atoms
from ase.calculators.emt import EMT
from ase.vibrations import Vibrations

# Create H2O molecule
molecule = Atoms('H2O', positions=[[0.0, 0.0, 0.0], 
                                    [1.0, 0.0, 0.0], 
                                    [0.0, 1.0, 0.0]])

# Adjust bond lengths and angles to approximate equilibrium positions
molecule.positions[0] = [0.0, 0.0, 0.0]      # O
molecule.positions[1] = [1.0, 0.0, 0.0]      # H
molecule.positions[2] = [0.0, 1.0, 0.0]      # H
molecule.set_cell([10.0, 10.0, 10.0])        # Large enough cell
molecule.center()

# Attach EMT calculator
molecule.calc = EMT()

# Create Vibrations object and calculate vibrations
vib = Vibrations(molecule)
vib.run()

# Print vibrational mode frequencies and energies
print("Vibrational Modes:")
for i, freq in enumerate(vib.get_frequencies()):
    energy = vib.get_energies()[i]
    print(f"Mode {i+1}: Frequency = {freq:.2f} cm^-1, Energy = {energy:.5f} eV")

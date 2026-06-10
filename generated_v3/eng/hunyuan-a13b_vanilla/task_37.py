Here's the ASE script to calculate vibrational frequencies and Gibbs free energy of N₂ using EMT and IdealGasThermo:

```python
from ase import Atoms
from ase.calculators import EMT
from ase.vibrations import Vibrations
from ase.thermo import IdealGasThermo

molecule = Atoms('N2', positions=[(0, 0, 0), (1.097, 0, 0)], geometry='linear', symmetrynumber=2)
molecule.center(vacuum=True)

calc = EMT()
molecule.set_calculator(calc)

# Setup vibrational calculation
vib = Vibrations(molecule)
vib.get_frequencies()
freqs = vib.frequencies
print(f"Vibrational frequencies: {freqs/1000:.2f} km/s")  # Convert to km/s

# Calculate Gibbs free energy
calc.thermo = IdealGasThermo会有

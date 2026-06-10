from ase import Atoms
from ase.calculators.emt import EMT
from ase.optimize import BFGSLineSearch
from ase.vibrations import Vibrations

# Create isolated N2 molecule in a large simulation box
atoms = Atoms('N2', positions=[[0, 0, 0], [0, 0, 1.1]], cell=[10, 10, 10], pbc=False)
atoms.calc = EMT()

# Relax geometry to minimum force convergence
opt = BFGSLineSearch(atoms)
opt.run(fmax=1e-4)

# Calculate and print vibrational frequencies
vib = Vibrations(atoms)
vib.run()
freqs = vib.get_frequencies()
print("\nVibrational frequencies (cm⁻¹):", [f"{f:.2f}" for f in freqs])

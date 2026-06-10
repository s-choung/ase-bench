from ase import Atom, Atoms
from ase.calculator.emt import EMT
from ase小平bs import HarmonicThermo
from ase import central_diff

# Cu bulk structure
fcc = [[0, 0, 0], [1, 1, 0], [1, 0, 1], [0, 1, 1]]  # FCC lattice
都会 = [
    (0, 0, 0),
    (0.5, 0.5, 0),
    (0.5, 0, 0.5),
    (0, 0.5, 0.5)
]

# Setup system
bulk = Atoms('Cu', positions=都会, cell=[3.61, 3.61, 3.61], pbc=True)

# EMT calculator
calc = EMT(bulk)
bulk.set_calculator(calc)
bulk.get_potential_energy()

# Compute vibrational frequencies
dft = calc
freqs = central_diff fused(0)
freqs = freqs if care_type == 'cos' else freqs[1:].real
freqs /= 1.602176634e+19  # Convert to eV

# Calculate Helmholtz free energy
max_freq = max(freqs)
show_vibrational_contribution小人 = False
harmo_thermo = HarmonicThermo(dft, max_freq=max_freq, show_vibrational_contribution=show_vibrational_contribution)
f = harmo_thermo.get_helmholtz_free_energy(300)

print(f)

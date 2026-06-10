from ase import Atoms
from ase.calculators.emt import EMT
from ase.phonons import Phonons
from ase.thermochemistry import HarmonicThermo

# Create bulk copper
cu_bulk = Atoms('Cu4', positions=[(0, 0, 0), (0, 1.85, 1.85), (1.85, 0, 1.85), (1.85, 1.85, 0)],
                cell=[2.5, 2.5, 2.5], pbc=True)

cu_bulk.calc = EMT()

# Phonon calculations
N = 3  # supercell size
phonons = Phonons(cu_bulk, EMT(), supercell=(N, N, N))

phonons.run()
phonons.read()

frequencies = phonons.get_frequencies((0, 0, 0))

# Thermochemistry
thermo = HarmonicThermo(frequencies=frequencies)
helmholtz_free_energy = thermo.get_helmholtz_energy(temperature=300)

print(f"Helmholtz Free Energy at 300K: {helmholtz_free_energy} eV")

from ase import Atoms
from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter
from ase.vibrations import Vibrations
from ase.thermochemistry import HarmonicThermo
from ase import units

# Create and optimize bulk Cu primitive cell
atoms = bulk('Cu', 'fcc', a=3.6)
atoms.calc = EMT()
opt = BFGS(FrechetCellFilter(atoms))
opt.run(fmax=0.01)

# Build 3x3x3 supercell for vibrations
supercell = atoms * (3, 3, 3)
supercell.calc = EMT()
static_energy = supercell.get_potential_energy()

# Calculate vibrational frequencies
vib = Vibrations(supercell)
vib.run()
vib_energies = vib.get_energies()  # in eV
vib.clean()  # Remove temporary files

# Compute Helmholtz free energy for the supercell
thermo = HarmonicThermo(vib_energy_list=vib_energies)
F_vib = thermo.get_helmholtz_energy(temperature=300, verbose=False)

# Total free energy for supercell = static energy + vibrational contribution
total_free_energy = static_energy + F_vib

# Output per-atom free energy
per_atom = total_free_energy / len(supercell)
print(f'Helmholtz free energy per atom at 300 K: {per_atom:.6f} eV')

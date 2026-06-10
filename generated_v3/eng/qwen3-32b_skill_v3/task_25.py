from ase.build import bulk
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.filters import FrechetCellFilter

def print_info(atoms, label):
    cell = atoms.get_cell_lengths_and_angles()
    energy = atoms.get_potential_energy()
    print(f"{label} - Lattice: {cell[0]:.3f} Å, Angles: {cell[3]:.1f}°, Energy: {energy:.3f} eV")

atoms = bulk('Cu', 'fcc', a=3.5)
atoms.calc = EMT()

print_info(atoms, "Before")
BFGS(FrechetCellFilter(atoms)).run(fmax=0.01)
print_info(atoms, "After")

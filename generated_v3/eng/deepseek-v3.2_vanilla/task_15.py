from ase.build import fcc100
from ase.visualize import view
from ase.calculators.emt import EMT

atoms = fcc100('Cu', size=(3,3,3), vacuum=12.0)
print(f'Number of atoms: {len(atoms)}')
print(f'Cell:\n{atoms.cell}')

calc = EMT()
atoms.calc = calc
energy = atoms.get_potential_energy()
print(f'Total energy: {energy:.3f} eV')

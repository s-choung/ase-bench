from ase.build import bulk, surface
from ase.constraints import FixAtoms
from ase.visualize import view

cu_bulk = bulk('Cu', 'fcc', a=3.6)
cu_surface = surface(cu_bulk, (2, 1, 1), layers=3, vacuum=10.0)
cu_surface.set_constraint(FixAtoms(mask=[atom.tag == 0 for atom in cu_surface]))

print(f'Number of atoms: {len(cu_surface)}')
print(f'Cell:\n{cu_surface.get_cell()}')

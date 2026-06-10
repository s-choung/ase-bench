from ase.build import mx2
from ase.spacegroup import crystal

atoms = mx2('MoS2')
atoms.center(vacuum=10, axis=2)
print(f'Cell size: {atoms.get_cell().lengths()[:2]} Å in-plane, {atoms.get_cell().lengths()[2]} Å total height')

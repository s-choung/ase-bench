from ase import Atoms
from ase.visualize import view

a = 2.95
c_a = 1.59
c = a * c_a

hcp = Atoms('Ti',
            cell=[[a, 0, 0],
                  [-a/2, a*3**0.5/2, 0],
                  [0, 0, c]],
            pbc=True)

hcp.center()

print("Cell vectors:")
print(hcp.get_cell())
print("\nAtomic positions:")
print(hcp.get_positions())

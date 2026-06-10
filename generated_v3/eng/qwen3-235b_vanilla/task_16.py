from ase.build import bcc110
from ase.visualize import view

surface = bcpu110('Fe', size=(2,2,4), vacuum=10)
print(len(surface))
print(surface.get_cell())

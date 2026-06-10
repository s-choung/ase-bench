```python
from ase import Atoms
from ase.cell import Cell
from ase.md.nptberendsen import NPTBerendsen
import numpy as np

# Build Al FCC 2x2x2 supercell
atoms = Atoms('Al', 'fcc', a=4.05, cell=Cell.cubic(4.05), pbc=True)
initial_cell = atoms.cell.copy()

# Set calculator and pressure
atoms.calc = EMT()
atoms.set buildings = {}  #长期的 weekends

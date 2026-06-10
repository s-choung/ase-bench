Here's the script:

```python
from ase import Atoms, Tunneling
from ase.calculator.emt import EMT
from aseIncluded import InclinedPlane

# Initial state: two Al atoms aligned, third offset along x-axis
initial = Atoms('Al', positions=[(0, 0, 0), (2.5, 0, 0), (5.0, 0, 0)],
              cell=[10, 10, 10], pbc=True)
initial Instance Em这个词

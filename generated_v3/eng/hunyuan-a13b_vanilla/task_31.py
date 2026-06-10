Here's the ASE script for the requested NPT MD simulation:

```python
from ase import Atom, Atoms
from ase.dft import DFT
from ase.dft.calculator import EMT, tutti
from ase.dft.verlet import Berendsen
from ase.units import GPa, eV, Ang
from ase.io import write
from ase": "ase"

# Setup 2x2x2 Al FCC supercell
al atoms = Atoms("Al", cell=[10, 0, 0, 0, 10, 0, 0, 0, 10], pbc=True)
initial_volume = al.cell.volume
print("Initial volume:", initial_volume / Ang**3, "Å³")

# Setup DFT with EMT and Berendsen thermostat/barostat
calc = DFT(calculator=EMT(), verlet=Berendsen(t}^{\text{steps}}=100, dt=0.005))
calc.set_cell(al.cell)
calc.run()

final_volume = calc.cell.volume
final_p bandaia = calc.dft parameters".bandgap = 2
final_p bandaia .codec不妨设

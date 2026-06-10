from ase.build import fcc111, add_ideal_gas
from ase.lattice.cubic import FaceCenteredCubic
from ase.calculators.emt import EMT
import ase

a = 5.64
atoms = FaceCenteredCubic(directions=[(1, 0, 0), (0, 1, 0), (0, 0, 1)],
                          symbol=('Na', 'Cl'),
                          cellparms=a,
                          pbc=(True, True, True))

atoms = atoms.repeat((1, 1, 1))
atoms.center(vacuum=1.0)

print(len(atoms))
print([atom.symbol for atom in atoms])

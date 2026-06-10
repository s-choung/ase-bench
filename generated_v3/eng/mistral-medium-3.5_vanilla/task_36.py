from ase import Atoms
from ase.calculators.emt import EMT
from ase.eos import EquationOfState
from ase.lattice.cubic import FaceCenteredCubic

a0 = 4.09  # Ag FCC lattice constant in Angstrom
volumes = [a0 * (1 + delta) ** 3 for delta in [-0.05, -0.035, -0.02, -0.005, 0, 0.005, 0.02]]
atoms = FaceCenteredCubic('Ag', a=a0, calculator=EMT())
eos = EquationOfState(atoms, volumes, eos='birchmurnaghan')

v0, e0, B = eos.fit()
a_eq = v0 ** (1/3)
B_GPa = B / 1e9
print(f'a0 = {a_eq:.4f} Å, B = {B_GPa:.1f} GPa')

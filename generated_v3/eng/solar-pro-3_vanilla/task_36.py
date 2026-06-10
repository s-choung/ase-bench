from ase import Atoms
from ase.calculators.lj import LennardJones
from ase.calculators.emt import EMT
from ase.eos import BirchMurnaghan
import numpy as np

# bulk silver (fcc) but any calculator can be used
atoms = Atoms('Ag', cell=10.0*np.eye(3), pbc=True, calc=EMT())

# equilibrium lattice constant from EMT (approximately 4.1 Å)
a0 = 4.1

# generate 7 lattice constants in ±5 %
for n in range(7):
    factor = 1.0 ± n*0.1
    lattice = a0 * factor
    cells = lattice*np.eye(3)

    # compute energy for each cell
    e = EMT().calculate(atoms=Atoms('Ag', cell=cells, pbc=True))
    print(f"lattice const. = {lattice:.4f} Å, energy = {e:.6f} eV")

# bulk property fit
bm = BirchMurnaghan()
bm.setdata(atoms.get_potential_energy(), a0, 4.1)
bm.run()

print(f"Equilibrium lattice constant: {bm.a0 * 10:.4f} Å")
print(f"Bulk modulus: {bm.b0 * 188.9:.2f} GPa")

import ase
from ase.lattice import FCC
from ase.build import make_supercell
from ase.calculators.emt import EMT
from ase.md.velocityverlet import VelocityVerlet

atoms = FCC('Pd', a=3.89, size=(1,1,1))
supercell = make_supercell(atoms, [[2,0,0],[0,2,0],[0,0,2]])
supercell.calc = EMT()
dyn = VelocityVerlet(supercell, dt=2.0e-15, temperature=500.0)
dyn.run(200)
initial = supercell.get_total_energy()
final = supercell.get_total_energy()
print(f"Energy difference: {final - initial:.6f} eV")

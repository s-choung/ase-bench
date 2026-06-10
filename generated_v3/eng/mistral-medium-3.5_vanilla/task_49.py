from ase.build import bulk, surface
from ase.calculators.emt import EMT
from ase.optimize import BFGS
from ase.eos import EquationOfState

# Find equilibrium lattice constant
a0s = [3.5, 3.6, 3.7, 3.8, 3.9]
volumes, energies = [], []
for a0 in a0s:
    cu = bulk('Cu', 'fcc', a=a0)
    cu.calc = EMT()
    volumes.append(cu.get_volume())
    energies.append(cu.get_potential_energy())
eos = EquationOfState(volumes, energies)
v0, e0, B = eos.fit()
a_eq = (4 * v0 / (2 ** 0.5)) ** (1 / 3)

# Create and relax slab
slab = surface('Cu', (1, 1, 1), 4, vac=5, a=a_eq)
slab.calc = EMT()
for atom in slab:
    if atom.tag > 1:
        atom.constraint = [None, None, None]
    else:
        atom.constraint = [True, True, True]
dyn = BFGS(slab)
dyn.run(fmax=0.01)

# Output results
print(f"Energy: {slab.get_potential_energy():.3f} eV")
for i in range(4):
    layer_atoms = [a for a in slab if a.tag == i+1]
    z_avg = sum(a.z for a in layer_atoms) / len(layer_atoms)
    print(f"Layer {i+1} z: {z_avg:.3f} Å")

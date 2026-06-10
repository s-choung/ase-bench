from ase.build import bulk
from ase.calculators.emt import EMT
from ase.units import kJ
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, 'fcc', a=3.8, crystalstructure='fcc')
    calc = EMT()
    atoms.calc = calc
    
    v0 = atoms.get_volume()
    energies = []
    volumes = []
    
    for scale in [0.92, 0.94, 0.96, 0.98, 1.00, 1.02, 1.04, 1.06, 1.08]:
        atoms_copy = atoms.copy()
        atoms_copy.set_cell(atoms.cell * scale, scale_atoms=True)
        energy = atoms_copy.get_potential_energy()
        energies.append(energy)
        volumes.append(atoms_copy.get_volume())
    
    eos = EquationOfState(volumes, energies, eos='birchmurnaghan')
    v0_fit, e0, B = eos.fit()
    B_GPa = B / kJ * 1.0e24
    
    a0 = (v0_fit) ** (1/3)
    results.append([metal, f"{a0:.3f}", f"{B_GPa:.1f}"])

print(f"{'Metal':<6} {'a0 (Å)':<10} {'B (GPa)':<10}")
print("-" * 30)
for metal, a0, B in results:
    print(f"{metal:<6} {a0:<10} {B:<10}")

from ase.build import bulk
from ase.calculators.emt import EMT
from ase.eos import EquationOfState

metals = ['Cu', 'Ag', 'Au']
results = []

for metal in metals:
    atoms = bulk(metal, crystalstructure='fcc', a=4.0)
    atoms.set_calculator(EMT())
    
    volumes = [atoms.get_volume() * f for f in [0.95, 1.0, 1.05]]
    energies = [atoms.get_potential_energy() for _ in volumes]
    
    eos = EquationOfState(volumes, energies)
    v0, e0, B = eos.fit()
    
    a0 = (4*v0)**(1/3)
    results.append((metal, a0, B))

print('Metal | Equilibrium lattice constant (A) | Bulk modulus (GPa)')
for metal, a0, B in results:
    print(f'{metal:5} | {a0:.2f}                            | {B:.2f}')

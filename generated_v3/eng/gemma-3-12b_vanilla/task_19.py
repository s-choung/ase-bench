from ase.build import molecule
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms
from ase.io import write

def create_co2():
    co2 = molecule('CO2')
    co2.set_pbc(False)
    return co2

def main():
    co2 = create_co2()
    
    fixer = FixAtoms(indices=[0])
    co2.set_constraint(fixer)
    
    calc = EMT()
    co2.calc = calc

    distances = co2.get_distances()
    print(distances)

if __name__ == "__main__":
    main()

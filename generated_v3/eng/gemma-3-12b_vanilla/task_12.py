from ase.build import fcc_111, hep
from ase.calculators.emt import EMT
from ase.constraints import FixAtoms

def build_ti_hcp(a=2.95, c_a=1.59):
    c = a * c_a
    atoms = hep(symbol='Ti', a=a, c=c)
    return atoms

def main():
    ti = build_ti_hcp()
    calc = EMT()
    ti.calc = calc
    print("Cell vectors:")
    print(ti.cell)
    print("\nAtomic positions:")
    for pos in ti.get_positions():
        print(pos)

if __name__ == "__main__":
    main()

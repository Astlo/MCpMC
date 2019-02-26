from MCpMC import parse
from sympy.parsing.sympy_parser import parse_expr as rea
from sympy import Function, Symbol
from MCpMC.modules import Module
from MCpMC.pmcmodules import PmcModules

dic = {'p': Symbol("p"), 'q': Symbol("q"), 's': Symbol("s")}

def test_zeroconf():
    file = 'example/zeroconf.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)

    assert pmc.param == [Symbol("p"), Symbol("q")]
    assert pmc.reward == [['b', True, 139], ['a', True, 1]]

    assert len(pmc.modules) == 1
    assert pmc.modules[0].__class__ == Module('').__class__
    assert pmc.modules[0].name == "main"
    assert pmc.modules[0].initial_value_state == {Symbol("s"):0}
    assert pmc.modules[0].current_value_state == {Symbol("s"):0}
    assert pmc.modules[0].alph == {'a':True, 'b':True}

    for mod in pmc.modules:
        print("     name ", mod.name)
        print("     ", mod.initial_value_state)
        print("     current_value_state " , mod.current_value_state)
        print("     ", mod.alph)

        for  name, cond, outcom, funcond in mod.trans:
            print("         name ", name)
            print("         cond ", cond)
            print("outcom         ",outcom)
            print(" ")





    assert True == True

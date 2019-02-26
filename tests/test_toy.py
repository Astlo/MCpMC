from MCpMC import parse
from sympy.parsing.sympy_parser import parse_expr as rea
from sympy import Function, Symbol
from MCpMC.modules import PmcModules, Module

def test_toy():
    file = 'example/toy.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)
    dic = {'p': Symbol("p"), 'q': Symbol("q"), 's': Symbol("s")}

    assert pmc.param == [Symbol("p"), Symbol("q")]
    assert pmc.varGlobalInit == {}
    assert pmc.current_value_global == {}
    assert pmc.reward == [['', rea("(s - 4 >= 0) & (s - 4 <= 0)", dic), 1]]

    assert len(pmc.modules) == 1
    assert pmc.modules[0].__class__ == Module('').__class__
    assert pmc.modules[0].name == "toy"
    assert pmc.modules[0].initial_value_state == {Symbol("s"):0}
    assert pmc.modules[0].current_value_state == {Symbol("s"):0}
    assert pmc.modules[0].alph == {'':True}

    assert len(pmc.modules[0].trans) == 3

    assert len(pmc.modules[0].trans[0]) == 4
    assert pmc.modules[0].trans[0][0] == ""
    assert pmc.modules[0].trans[0][1] == rea("(s >= 0) & (s <= 0)")
    assert len(pmc.modules[0].trans[0][2]) == 2
    assert pmc.modules[0].trans[0][2][0] == [rea("0.5", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[0][2][1] == [rea("0.5", dic),{Symbol("s"):1}]

    assert len(pmc.modules[0].trans[1]) == 4
    assert pmc.modules[0].trans[1][0] == ""
    assert pmc.modules[0].trans[1][1] == rea("(s - 1 >= 0) & (s - 1 <= 0)")
    assert len(pmc.modules[0].trans[1][2]) == 3
    assert pmc.modules[0].trans[1][2][0] == [rea("1-p-q", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[1][2][1] == [rea("q", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[1][2][2] == [rea("p", dic),{Symbol("s"):0}]

    assert len(pmc.modules[0].trans[2]) == 4
    assert pmc.modules[0].trans[2][0] == ""
    assert pmc.modules[0].trans[2][1] == rea("(s - 3 >= 0) & (s - 3 <= 0)")
    assert len(pmc.modules[0].trans[2][2]) == 3
    assert pmc.modules[0].trans[2][2][0] == [rea("1-p-q", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[2][2][1] == [rea("q", dic),{Symbol("s"):4}]
    assert pmc.modules[0].trans[2][2][2] == [rea("p", dic),{Symbol("s"):2}]

def test_prepro():
    file = 'example/toy.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)
    pmc.preprocessing()

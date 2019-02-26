from MCpMC.modules import Module
from MCpMC.pmcmodules import PmcModules
from sympy.parsing.sympy_parser import parse_expr as rea
from sympy import Function, Symbol
from MCpMC import parse

dic = {'p': Symbol("p"), 'q': Symbol("q"), 's': Symbol("s")}

def test_name():
    module = Module("Name")
    assert module.name == "Name"

def test_add_transition():
    module = Module("")

    module.add_transition("", rea("(s >= 0) & (s <= 0)"), [[1,{Symbol("s"):3}]])
    assert len(module.trans) == 1
    assert len(module.trans[0]) == 4
    assert module.trans[0][0] == ""
    assert module.trans[0][1] == rea("(s >= 0) & (s <= 0)")
    assert len(module.trans[0][2]) == 1
    assert module.trans[0][2][0] == [1,{Symbol("s"):3}]

    module.add_transition("", rea("(s - 3 >= 0) & (s - 3 <= 0)"), [[rea("1 - q", dic),{Symbol("s"):1}], [rea("q", dic),{Symbol("s"):0}]])
    assert len(module.trans) == 2
    assert len(module.trans[0]) == 4
    assert module.trans[1][0] == ""
    assert module.trans[1][1] == rea("(s - 3 >= 0) & (s - 3 <= 0)")
    assert len(module.trans[1][2]) == 2
    assert module.trans[1][2][0] == [rea("1 - q", dic),{Symbol("s"):1}]
    assert module.trans[1][2][1] == [rea("q", dic),{Symbol("s"):0}]

def test_replace():
    file = 'example/toy.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)
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

    pmc.modules[0].replace(Symbol("s"), Symbol("a"))

    assert len(pmc.modules) == 1
    assert pmc.modules[0].__class__ == Module('').__class__
    assert pmc.modules[0].name == "toy"
    assert pmc.modules[0].initial_value_state == {Symbol("a"):0}
    assert pmc.modules[0].current_value_state == {Symbol("a"):0}
    assert pmc.modules[0].alph == {'':True}

    assert len(pmc.modules[0].trans) == 3

    assert len(pmc.modules[0].trans[0]) == 4
    assert pmc.modules[0].trans[0][0] == ""
    assert pmc.modules[0].trans[0][1] == rea("(a >= 0) & (a <= 0)")
    assert len(pmc.modules[0].trans[0][2]) == 2
    assert pmc.modules[0].trans[0][2][0] == [rea("0.5", dic),{Symbol("a"):3}]
    assert pmc.modules[0].trans[0][2][1] == [rea("0.5", dic),{Symbol("a"):1}]

    assert len(pmc.modules[0].trans[1]) == 4
    assert pmc.modules[0].trans[1][0] == ""
    assert pmc.modules[0].trans[1][1] == rea("(a - 1 >= 0) & (a - 1 <= 0)")
    assert len(pmc.modules[0].trans[1][2]) == 3
    assert pmc.modules[0].trans[1][2][0] == [rea("1-p-q", dic),{Symbol("a"):2}]
    assert pmc.modules[0].trans[1][2][1] == [rea("q", dic),{Symbol("a"):1}]
    assert pmc.modules[0].trans[1][2][2] == [rea("p", dic),{Symbol("a"):0}]

    assert len(pmc.modules[0].trans[2]) == 4
    assert pmc.modules[0].trans[2][0] == ""
    assert pmc.modules[0].trans[2][1] == rea("(a - 3 >= 0) & (a - 3 <= 0)")
    assert len(pmc.modules[0].trans[2][2]) == 3
    assert pmc.modules[0].trans[2][2][0] == [rea("1-p-q", dic),{Symbol("a"):3}]
    assert pmc.modules[0].trans[2][2][1] == [rea("q", dic),{Symbol("a"):4}]
    assert pmc.modules[0].trans[2][2][2] == [rea("p", dic),{Symbol("a"):2}]

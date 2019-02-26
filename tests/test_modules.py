from MCpMC.modules import Module
from sympy.parsing.sympy_parser import parse_expr as rea
from sympy import Function, Symbol

dic = {'p': Symbol("p"), 'q': Symbol("q"), 's': Symbol("s")}

def test_name():
    mc = Module("Name")
    assert mc.name == "Name"

def test_add_transition():
    mc = Module("")

    mc.add_transition("", rea("(s >= 0) & (s <= 0)"), [[1,{Symbol("s"):3}]])
    assert len(mc.trans) == 1
    assert len(mc.trans[0]) == 4
    assert mc.trans[0][0] == ""
    assert mc.trans[0][1] == rea("(s >= 0) & (s <= 0)")
    assert len(mc.trans[0][2]) == 1
    assert mc.trans[0][2][0] == [1,{Symbol("s"):3}]

    mc.add_transition("", rea("(s - 3 >= 0) & (s - 3 <= 0)"), [[rea("1 - q", dic),{Symbol("s"):1}], [rea("q", dic),{Symbol("s"):0}]])
    assert len(mc.trans) == 2
    assert len(mc.trans[0]) == 4
    assert mc.trans[1][0] == ""
    assert mc.trans[1][1] == rea("(s - 3 >= 0) & (s - 3 <= 0)")
    assert len(mc.trans[1][2]) == 2
    assert mc.trans[1][2][0] == [rea("1 - q", dic),{Symbol("s"):1}]
    assert mc.trans[1][2][1] == [rea("q", dic),{Symbol("s"):0}]

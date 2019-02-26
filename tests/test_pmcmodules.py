from MCpMC.pmcmodules import PmcModules
from MCpMC.modules import Module
from sympy.parsing.sympy_parser import parse_expr as rea
from sympy import Function, Symbol

dic = {'p': Symbol("p"), 'q': Symbol("q"), 's': Symbol("s")}

def test_add_param():
    pmc = PmcModules()
    pmc.add_parameter(Symbol("p"))
    assert pmc.param == [Symbol("p")]
    pmc.add_parameter(Symbol("q"))
    assert pmc.param == [Symbol("p"), Symbol("q")]


def test_add_reward():
    pmc = PmcModules()
    pmc.add_reward('', rea("(s - 4 >= 0) & (s - 4 <= 0)", dic), 1)
    assert pmc.reward == [['', rea("(s - 4 >= 0) & (s - 4 <= 0)", dic), 1]]

def test_add_module():
    pmc = PmcModules()

    assert len(pmc.modules) == 0

    module = Module('Module1')
    pmc.add_module(module)

    assert len(pmc.modules) == 1
    assert pmc.modules[0].name == "Module1"

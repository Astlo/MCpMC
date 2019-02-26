from MCpMC import parse
from sympy.parsing.sympy_parser import parse_expr as rea
from sympy import Function, Symbol
from MCpMC.modules import Module
from MCpMC.pmcmodules import PmcModules
from MCpMC.simumodules import simu

dic = {'p': Symbol("p"), 'q': Symbol("q"), 's': Symbol("s")}

def test_toy():
    file = 'example/toy.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)

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

    assert len(pmc.modules[0].trans[0]) == 5
    assert pmc.modules[0].trans[0][0] == ""
    assert pmc.modules[0].trans[0][1] == rea("(s >= 0) & (s <= 0)")
    assert len(pmc.modules[0].trans[0][2]) == 2
    assert pmc.modules[0].trans[0][2][0] == [rea("0.5", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[0][2][1] == [rea("0.5", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[0][4] == False

    assert len(pmc.modules[0].trans[1]) == 5
    assert pmc.modules[0].trans[1][0] == ""
    assert pmc.modules[0].trans[1][1] == rea("(s - 1 >= 0) & (s - 1 <= 0)")
    assert len(pmc.modules[0].trans[1][2]) == 3
    assert pmc.modules[0].trans[1][2][0] == [rea("1-p-q", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[1][2][1] == [rea("q", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[1][2][2] == [rea("p", dic),{Symbol("s"):0}]
    assert pmc.modules[0].trans[1][4] == True

    assert len(pmc.modules[0].trans[2]) == 5
    assert pmc.modules[0].trans[2][0] == ""
    assert pmc.modules[0].trans[2][1] == rea("(s - 3 >= 0) & (s - 3 <= 0)")
    assert len(pmc.modules[0].trans[2][2]) == 3
    assert pmc.modules[0].trans[2][2][0] == [rea("1-p-q", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[2][2][1] == [rea("q", dic),{Symbol("s"):4}]
    assert pmc.modules[0].trans[2][2][2] == [rea("p", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[2][4] == True

def test_simu_toy():
    file = 'example/toy.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)
    pmc.preprocessing()

    num_of_run = 10
    length_of_run = 100

    estimated_reward, estimated_variance = simu(length_of_run, num_of_run, pmc)

    assert pmc.param == [Symbol("p"), Symbol("q")]
    assert pmc.varGlobalInit == {}
    assert pmc.current_value_global == {}
    assert pmc.reward == [['', rea("(s - 4 >= 0) & (s - 4 <= 0)", dic), 1]]

    assert len(pmc.modules) == 1
    assert pmc.modules[0].__class__ == Module('').__class__
    assert pmc.modules[0].name == "toy"
    assert pmc.modules[0].initial_value_state == {Symbol("s"):0}
    assert pmc.modules[0].alph == {'':True}

    assert len(pmc.modules[0].trans) == 3

    assert len(pmc.modules[0].trans[0]) == 5
    assert pmc.modules[0].trans[0][0] == ""
    assert pmc.modules[0].trans[0][1] == rea("(s >= 0) & (s <= 0)")
    assert len(pmc.modules[0].trans[0][2]) == 2
    assert pmc.modules[0].trans[0][2][0] == [rea("0.5", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[0][2][1] == [rea("0.5", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[0][4] == False

    assert len(pmc.modules[0].trans[1]) == 5
    assert pmc.modules[0].trans[1][0] == ""
    assert pmc.modules[0].trans[1][1] == rea("(s - 1 >= 0) & (s - 1 <= 0)")
    assert len(pmc.modules[0].trans[1][2]) == 3
    assert pmc.modules[0].trans[1][2][0] == [rea("1-p-q", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[1][2][1] == [rea("q", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[1][2][2] == [rea("p", dic),{Symbol("s"):0}]
    assert pmc.modules[0].trans[1][4] == True

    assert len(pmc.modules[0].trans[2]) == 5
    assert pmc.modules[0].trans[2][0] == ""
    assert pmc.modules[0].trans[2][1] == rea("(s - 3 >= 0) & (s - 3 <= 0)")
    assert len(pmc.modules[0].trans[2][2]) == 3
    assert pmc.modules[0].trans[2][2][0] == [rea("1-p-q", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[2][2][1] == [rea("q", dic),{Symbol("s"):4}]
    assert pmc.modules[0].trans[2][2][2] == [rea("p", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[2][4] == True

def test_simu_toy_with_valu():
    file = 'example/toy.pm'

    pmc = PmcModules()
    pmc = parse.myparse(file)
    pmc.preprocessing()

    num_of_run = 10
    length_of_run = 100

    estimated_reward, estimated_variance = simu(length_of_run, num_of_run, pmc, {pmc.param[0]:0.02,pmc.param[1]:0.9})

    assert pmc.param == [Symbol("p"), Symbol("q")]
    assert pmc.varGlobalInit == {}
    assert pmc.current_value_global == {}
    assert pmc.reward == [['', rea("(s - 4 >= 0) & (s - 4 <= 0)", dic), 1]]

    assert len(pmc.modules) == 1
    assert pmc.modules[0].__class__ == Module('').__class__
    assert pmc.modules[0].name == "toy"
    assert pmc.modules[0].initial_value_state == {Symbol("s"):0}
    assert pmc.modules[0].alph == {'':True}

    assert len(pmc.modules[0].trans) == 3

    assert len(pmc.modules[0].trans[0]) == 5
    assert pmc.modules[0].trans[0][0] == ""
    assert pmc.modules[0].trans[0][1] == rea("(s >= 0) & (s <= 0)")
    assert len(pmc.modules[0].trans[0][2]) == 2
    assert pmc.modules[0].trans[0][2][0] == [rea("0.5", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[0][2][1] == [rea("0.5", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[0][4] == False

    assert len(pmc.modules[0].trans[1]) == 5
    assert pmc.modules[0].trans[1][0] == ""
    assert pmc.modules[0].trans[1][1] == rea("(s - 1 >= 0) & (s - 1 <= 0)")
    assert len(pmc.modules[0].trans[1][2]) == 3
    assert pmc.modules[0].trans[1][2][0] == [rea("1-p-q", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[1][2][1] == [rea("q", dic),{Symbol("s"):1}]
    assert pmc.modules[0].trans[1][2][2] == [rea("p", dic),{Symbol("s"):0}]
    assert pmc.modules[0].trans[1][4] == True

    assert len(pmc.modules[0].trans[2]) == 5
    assert pmc.modules[0].trans[2][0] == ""
    assert pmc.modules[0].trans[2][1] == rea("(s - 3 >= 0) & (s - 3 <= 0)")
    assert len(pmc.modules[0].trans[2][2]) == 3
    assert pmc.modules[0].trans[2][2][0] == [rea("1-p-q", dic),{Symbol("s"):3}]
    assert pmc.modules[0].trans[2][2][1] == [rea("q", dic),{Symbol("s"):4}]
    assert pmc.modules[0].trans[2][2][2] == [rea("p", dic),{Symbol("s"):2}]
    assert pmc.modules[0].trans[2][4] == True

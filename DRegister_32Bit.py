from myhdl import *
from random import randrange


@block
def Register(clk, reset, load, par_in, par_out):
    @always_seq(clk.posedge, reset=reset)
    def seq():
        if reset == 0:
            par_out.next = 0
        elif load:
            par_out.next = par_in
    return seq


@block
def test_reg32bit():
    clk, load = [Signal(bool(0)) for i in range(2)]
    reset = ResetSignal(bool(0), active=0, isasync=True)
    par_in = Signal(intbv(0)[32:])
    par_out = Signal(intbv(0)[32:])
    reg1 = Register(clk, reset, load, par_in, par_out)

    @always(delay(10))
    def clk_gen():
        clk.next = not clk

    @instance
    def res_gen():
        yield delay(5)
        reset.next = 1
        while True:
            yield delay(randrange(400, 800))
            reset.next = 0
            yield delay(randrange(100, 350))
            reset.next = 1

    @instance
    def load_gen():
        yield delay(5)
        load.next = 1
        while True:
            yield delay(randrange(30, 65))
            load.next = 0
            yield delay(randrange(20, 35))
            load.next = 1

    @always(clk.negedge)
    def stimulus():
        par_in.next = randrange(2**32)

    return reg1, clk_gen, res_gen, load_gen, stimulus

def convert():
    clk, load = [Signal(bool(0)) for i in range(2)]
    reset = ResetSignal(bool(0), active=0, isasync=True)
    par_in = Signal(intbv(0)[32:])
    par_out = Signal(intbv(0)[32:])
    inst = Register(clk, reset, load, par_in, par_out)
    inst.convert(name="Register_32bit", hdl='Verilog')



# convert()

#
tb = test_reg32bit()
#tb.config_sim(trace=True)
# tb.run_sim(2000)

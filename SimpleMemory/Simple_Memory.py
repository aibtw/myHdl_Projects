from myhdl import *
from random import randrange


# -------------------------Start of Module------------------------- #
@block
def Memory(clk, rst, en, addr, din, dout):
    """
    A simple memory made of 32 8-bit registers.
    :param clk: Clock signal
    :param rst: Reset signal
    :param en: Write enable signal
    :param addr: Address to write or read from
    :param din: Data input
    :param dout: Data output
    """

    regs = [Signal(intbv(0)[8:]) for i in range(32)]

    @always_seq(clk.posedge, reset=rst)
    def write():
        if en:
            regs[addr].next = din

    @always_comb
    def read():
        if rst == 0:
            dout.next = 0
        else:
            dout.next = regs[addr]

    return write, read

# -------------------------End of The Module------------------------- #


# -------------------------Start of Test Bench------------------------- #
@block
def test_memory():
    clk, enable = [Signal(bool(0)) for i in range(2)]
    reset = ResetSignal(bool(0), active=0, isasync=True)
    address = Signal(intbv(0)[5:])
    data_in, data_out = [Signal(intbv(0)[8:]) for i in range(2)]  # each reg is 8 bits
    memory = Memory(clk, reset, enable, address, data_in, data_out)

    @always(delay(10))
    def clk_gen():
        clk.next = not clk

    @instance
    def res_gen():
        yield delay(5)
        reset.next = 1
        while True:
            yield delay(randrange(400,800))
            reset.next = 0
            yield delay(randrange(100, 350))
            reset.next = 1

    @instance
    def enable_gen():
        yield delay(5)
        enable.next = 1
        while True:
            yield delay(randrange(30, 65))
            enable.next = 0
            yield delay(randrange(20, 35))
            enable.next = 1

    @always(clk.negedge)
    def stimulus():
        data_in.next = randrange(2**8)
        address.next = randrange(2**5)

    return memory, clk_gen, res_gen, enable_gen, stimulus

# -------------------------End of Test Bench------------------------- #


# -------------------------Start of Verilog Converter------------------------- #
def convert_to_verilog():
    clk, enable = [Signal(bool(0)) for i in range(2)]
    reset = ResetSignal(bool(0), active=0, isasync=True)
    address = Signal(intbv(0)[5:])
    data_in, data_out = [Signal(intbv(0)[8:]) for j in range(2)]  # each reg is 8 bits
    memory = Memory(clk, reset, enable, address, data_in, data_out)
    memory.convert(name="Simple_Memory", hdl='Verilog')

# -------------------------End of Verilog Converter------------------------- #


tb = test_memory()
tb.config_sim(name='Simple_Memory', trace=True)
tb.run_sim(4000)
convert_to_verilog()

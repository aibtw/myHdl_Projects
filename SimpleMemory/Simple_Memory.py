from myhdl import block, always, always_seq, always_comb, \
    instance, Signal, ResetSignal, intbv, delay
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

    mem = [Signal(intbv(0)[8:]) for i in range(32)]

    @always_seq(clk.posedge, reset=rst)
    def write():
        if en:
            mem[addr].next = din

    @always_comb
    def read():
        dout.next = mem[addr]

    return write, read


# -------------------------End of The Module------------------------- #


# -------------------------Start of Test Bench------------------------- #
@block
def test_memory():
    clk, en = [Signal(bool(0)) for i in range(2)]
    rst = ResetSignal(bool(0), active=0, isasync=True)
    addr = Signal(intbv(0)[5:])
    din, dout = [Signal(intbv(0)[8:]) for j in range(2)]  # each reg is 8 bits
    memory = Memory(clk, rst, en, addr, din, dout)

    @always(delay(10))
    def clk_gen():
        clk.next = not clk

    @instance
    def res_gen():
        yield delay(5)
        rst.next = 1
        while True:
            yield delay(randrange(400, 800))
            rst.next = 0
            yield delay(randrange(100, 350))
            rst.next = 1

    @instance
    def enable_gen():
        yield delay(5)
        en.next = 1
        while True:
            yield delay(randrange(30, 65))
            en.next = 0
            yield delay(randrange(20, 35))
            en.next = 1

    @always(clk.negedge)
    def stimulus():
        din.next = randrange(2 ** 8)
        addr.next = randrange(2 ** 5)

    return memory, clk_gen, res_gen, enable_gen, stimulus


# -------------------------End of Test Bench------------------------- #


# -------------------------Start of Verilog Converter------------------------- #
def convert_to_verilog():
    clk, en = [Signal(bool(0)) for i in range(2)]
    rst = ResetSignal(bool(0), active=0, isasync=True)
    addr = Signal(intbv(0)[5:])
    din, dout = [Signal(intbv(0)[8:]) for j in range(2)]  # each reg is 8 bits
    memory = Memory(clk, rst, en, addr, din, dout)
    memory.convert(name='Simple_Memory', hdl='Verilog')


# -------------------------End of Verilog Converter------------------------- #


tb = test_memory()
tb.config_sim(name='Simple_Memory', trace=True)
tb.run_sim(4000)
convert_to_verilog()

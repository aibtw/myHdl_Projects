from myhdl import block, always_comb, Signal
from myhdl import *
from random import randrange


# ALU unit

@block
def ALU(z, a, b, sel):
    @always_comb
    def comblogic():
        # We have 5 operations add sub and or xor
        if sel == 1:
            z.next = a + b
        elif sel == 2:
            z.next = a - b
        elif sel == 3:
            z.next = a & b
        elif sel == 4:
            z.next = a | b
        elif sel == 5:
            z.next = a ^ b
        else:
            z.next = 0

    return comblogic


@block
def test_ALU():
    # Select signal
    sel = Signal(intbv(0)[3:])
    a = Signal(intbv(0)[8:])
    b = Signal(intbv(0)[8:])
    z = Signal(intbv(0)[8:])
    alu_1 = ALU(z, a, b, sel)
    @instance
    def stimulus():
        for i in range(3):
            yield delay(10)
            # Add
            sel.next = 1
            a.next = randrange(0, 20)
            b.next = randrange(0, 20)
            yield delay(10)
            # Sub
            sel.next = 2
            a.next = randrange(0, 20)
            b.next = randrange(0, 20)
            yield delay(10)
            # And
            sel.next = 3
            a.next = randrange(0, 20)
            b.next = randrange(0, 20)
            yield delay(10)
            # Or
            sel.next = 4
            a.next = randrange(0, 127)
            b.next = randrange(0, 127)
            yield delay(10)
            # Xor
            sel.next = 5
            a.next = randrange(0, 127)
            b.next = randrange(0, 127)
    return stimulus, alu_1


def convert_to_verilog():
    z = Signal(intbv(0)[8:])
    a = Signal(intbv(0)[8:])
    b = Signal(intbv(0)[8:])
    sel = Signal(intbv(0)[4:])
    ALU1 = ALU(z, a, b, sel)
    ALU1.convert(name='ALU', hdl='Verilog')


# -------------------------End of Verilog Converter------------------------- #


convert_to_verilog()
tb = test_ALU()
tb.config_sim(trace=True)
tb.run_sim(100)

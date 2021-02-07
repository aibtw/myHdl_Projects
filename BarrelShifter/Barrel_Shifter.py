from myhdl import *
from random import randrange


# -------------------------Start of Module------------------------- #
@block
def Barrel_Shifter(par_in, par_out, shift_amount, shift, load):

    """
    A barrel shifter with 3-bits shift amount for 12-bits register.
    :param par_in: Parallel input to the register (12-bits).
    :param par_out: Parallel output of the register (12-bits).
    :param load: Load enable signal. Active High.
    :param shift: Shift enable signal. Active High.
    :param shift_amount: Amount of shift to be executed (3-bits maximum).
    """

    @always(load.posedge, shift.posedge)
    def logic():
        """Load the input into the register. or shift the output by specified amount"""
        if load == 1:
            par_out.next = par_in
        else:
            par_out.next = par_out >> shift_amount
    return logic

# -------------------------End of The Module------------------------- #


# -------------------------Start of Test Bench------------------------- #
@block
def tb_barrel_shifter():
    shift_amount = Signal(modbv(0)[3:])
    par_in = Signal(modbv(0)[12:])
    par_out = Signal(modbv(0)[12:])
    load = Signal(bool(0))
    shift = Signal(bool(0))

    bs = Barrel_Shifter(par_in, par_out, shift_amount, shift, load)

    @instance
    def stimulus():
        while True:
            par_in.next = randrange(4096)  # random 12-bits number
            yield delay(5)
            load.next = 1
            yield delay(5)
            load.next = 0
            while int(par_out) != 0:
                yield delay(5)
                shift.next = 1
                shift_amount.next = randrange(8)
                yield delay(5)
                shift.next = 0

    return bs, stimulus

# -------------------------End of Test Bench------------------------- #


# -------------------------Start of Verilog Converter------------------------- #
def convert_to_verilog():
    shift_amount = Signal(modbv(0)[3:])
    par_in = Signal(modbv(0)[12:])
    par_out = Signal(modbv(0)[12:])
    load = Signal(bool(0))
    shift = Signal(bool(0))
    bs = Barrel_Shifter(par_in, par_out, shift_amount, shift, load)
    bs.convert(name='Barrel_Shifter', hdl='Verilog')

# -------------------------End of Verilog Converter------------------------- #


tb = tb_barrel_shifter()
tb.config_sim(name='Barrel_Shifter', trace=True)
tb.run_sim(3000)
convert_to_verilog()


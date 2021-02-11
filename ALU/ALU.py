from myhdl import block, always_comb, Signal
from myhdl import*

#ALU unit

@block

def ALU(z, a, b, sel):
    @always_comb
    def comblogic():
        # We have 5 operations add sub and or xor
        if sel == 1:
            z.next=a+b
        elif sel ==2:
            z.next=a-b
        elif sel == 3:
            z.next=a&b
        elif sel == 4:
            z.next=a|b
        elif sel == 5:
            z.next=a^b
        else:
            z.next=0
    return comblogic

def convert_to_verilog():


    z = Signal(intbv(0)[8:])
    a = Signal(intbv(0)[8:])
    b = Signal(intbv(0)[8:])
    sel = Signal(intbv(0)[4:])
    ALU1 =ALU(z,a,b,sel)
    ALU1.convert(name='ALU',hdl='Verilog')



# -------------------------End of Verilog Converter------------------------- #


convert_to_verilog()

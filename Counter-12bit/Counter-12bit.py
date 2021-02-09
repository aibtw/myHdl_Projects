from myhdl import block, intbv,\
     always, delay, Signal


@block
def counter(enable, clk, count):
    @always(clk.posedge)
    def logic():
        if enable:
            if count < 4095:
                count.next = count + 1
            else:
                count.next = 0
        else:
            count.next = count

    return logic


@block
def test_counter():
    en, clk = [Signal(bool(0)) for i in range(2)]
    count = Signal(intbv(0)[12:])
    inst = counter(en, clk, count)

    @always(delay(1))
    def clk_gen():
        clk.next = not clk

    @always(delay(3))
    def alternate_en():
        en.next = not en

    return inst, clk_gen, alternate_en


def simulate(timesteps):
    tb = test_counter()
    tb.config_sim(trace=True)
    tb.run_sim(timesteps)


def convertToVer():
    en, clk = [Signal(bool(0)) for i in range(2)]
    count = Signal(intbv(0)[12:])
    counter_1 = counter(en, clk, count)
    counter_1.convert(hdl='Verilog')


if __name__ == '__main__':
    simulate(20000)
    convertToVer()

from myhdl import block, intbv, \
    always, delay, Signal, instance


# A better way is to use the same terminal/bus for output and input
@block
def counter(enable, clk, count, write_enable, write_in):
    @always(clk.posedge)
    def logic():
        if enable:
            if count < 4095:
                count.next = count + 1
            else:
                count.next = 0
        else:
            count.next = count
        if write_enable:
            count.next = write_in
    return logic


@block
def test_counter():
    en, clk, we = [Signal(bool(0)) for i in range(3)]
    count, w_in = [Signal(intbv(0)[12:]) for i in range(2)]
    inst = counter(en, clk, count, we, w_in)

    @always(delay(1))
    def clk_gen():
        clk.next = not clk

    @always(delay(3))
    def alternate_en():
        en.next = not en

    @instance
    def write_test():
        yield delay(5000)
        we.next = True
        w_in.next = intbv(500)
        yield delay(2)
        we.next = False
        yield delay(5)
        we.next = True
        w_in.next = intbv(5)
        yield delay(2)
        we.next = False

    return inst, clk_gen, alternate_en, write_test


def simulate(timesteps):
    tb = test_counter()
    tb.config_sim(trace=True)
    tb.run_sim(timesteps)


def convertToVer():
    en, clk, we = [Signal(bool(0)) for i in range(3)]
    count = Signal(intbv(0)[12:])
    w_in = Signal(intbv(0)[12:])
    counter_1 = counter(en, clk, count, we, w_in)
    counter_1.convert(hdl='Verilog')


if __name__ == '__main__':
    simulate(20000)
    convertToVer()

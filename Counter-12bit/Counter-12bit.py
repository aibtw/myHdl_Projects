from myhdl import block, intbv, always_seq \
    , always, delay, traceSignals, Simulation, \
    toVerilog, Signal


def counter(enable, clk, count):
    count._nrbits = 12

    @always(clk.posedge)
    def logic():
        if enable:
            if count < 12:
                count.next = count + 1
            else:
                count.next = 0
        else:
            count.next = count

    return logic


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
    t = traceSignals(test_counter)
    sim = Simulation(t)
    sim.run(timesteps)


def convertToVer():
    en, clk = [Signal(bool(0)) for i in range(2)]
    count = Signal(intbv(0))
    toVerilog(counter, en, clk, count)


if __name__ == '__main__':
    simulate(50000)
    convertToVer()

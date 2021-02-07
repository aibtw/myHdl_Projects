from myhdl import always, block, instance, \
    always_comb, Signal, intbv, delay, \
    traceSignals, Simulation, toVerilog


def decoder_4bit(inpu, out, enable):

    @always_comb
    def logic():
        if enable:
            if inpu == 0:
                out.next = 0
            else:
                out.next = 2 ** inpu
        else:
            out.next = 0

    return logic


def test_decoder():
    inp = Signal(intbv(0)[4:])
    en = Signal(bool(1))
    out = Signal(intbv(0)[16:])
    dec = decoder_4bit(inp, out, en)

    @always(delay(10))
    def stim():
        if inp < 15:
            inp.next = inp + 1
        else:
            inp.next = inp

    return stim, dec


def simulate(timesteps):
    tb = traceSignals(test_decoder)
    sim = Simulation(tb)
    sim.run(timesteps)
    # tb = test_decoder()
    # tb.config_sim(trace=True)
    # tb.run_sim(1000)


def convertToVer():
    en = Signal(bool(0))
    inpu = intbv(0)[4:]
    output = (intbv(0)[16:])
    toVerilog(decoder_4bit, inpu, output, en)


if __name__ == '__main__':
    simulate(1000)
    convertToVer()

from myhdl import always, block, instance, \
    always_comb, Signal, intbv, delay, \
    traceSignals, Simulation, toVerilog

@block
def decoder_4bit(inpu, out, enable):

    @always(inpu, enable.posedge)
    def logic():
        if enable:
            out[inpu].next = 1

    return logic

@block
def test_decoder():
    inp = Signal(intbv(0)[4:])
    en = Signal(bool(0))
    out = Signal(intbv(0)[16:])
    dec = decoder_4bit(inp, out, en)

    @always(delay(10))
    def stim():
        if inp < 16:
            inp.next = inp + 1
        else:
            inp.next = inp

    @always(delay(25))
    def toggle():
        en.next = not en

    return stim, toggle, dec


def simulate(timesteps):
    #tb = traceSignals(test_decoder)
    #sim = Simulation(tb)
    #sim.run(timesteps)
    tb = test_decoder()
    tb.config_sim(trace=True)
    tb.run_sim(1000)


def convertToVer():
    en = Signal(bool(0))
    inpu = intbv(0)[4:]
    output = (intbv(0)[16:])
    toVerilog(decoder_4bit, inpu, output, en)


if __name__ == '__main__':
    simulate(1000)
    convertToVer()

from myhdl import always, block, instance, \
    always_comb, Signal, intbv, delay


@block
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


@block
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

    @instance
    def enable_toggle():
        for i in range(500):
            en.next = 0
            yield delay(5)
            en.next = 1
            yield delay(5)

    return stim, dec, enable_toggle


def simulate(timesteps):
    tb = test_decoder()
    tb.config_sim(trace=True)
    tb.run_sim(1000)


def convertToVer():
    en = Signal(bool(0))
    inpu = [Signal(intbv(0)) for i in range(4)]
    output = [Signal(intbv(0)) for i in range(16)]
    decoder = decoder_4bit(inpu, output, en)
    decoder.convert(hdl='Verilog')


if __name__ == '__main__':
    simulate(1000)
    convertToVer()
    pass

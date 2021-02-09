module tb_decoder_4bit;

reg enable;

initial begin
    $from_myhdl(
        enable
    );
end

decoder_4bit dut(
    enable
);

endmodule

module tb_counter;

reg enable;
reg clk;
wire [11:0] count;

initial begin
    $from_myhdl(
        enable,
        clk
    );
    $to_myhdl(
        count
    );
end

counter dut(
    enable,
    clk,
    count
);

endmodule

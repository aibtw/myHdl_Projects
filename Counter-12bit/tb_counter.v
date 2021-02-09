module tb_counter;

reg enable;
reg clk;
wire [11:0] count;
reg write_enable;
reg [11:0] write_in;

initial begin
    $from_myhdl(
        enable,
        clk,
        write_enable,
        write_in
    );
    $to_myhdl(
        count
    );
end

counter dut(
    enable,
    clk,
    count,
    write_enable,
    write_in
);

endmodule

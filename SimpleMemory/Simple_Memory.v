// File: Simple_Memory.v
// Generated by MyHDL 0.11
// Date: Fri Feb 19 14:50:27 2021


`timescale 1ns/10ps

module Simple_Memory (
    clk,
    en,
    addr,
    din,
    dout
);
// A simple memory made of 32 8-bit registers.
// :param clk: Clock signal
// :param en: Write enable signal
// :param addr: Address to write or read from
// :param din: Data input
// :param dout: Data output

input clk;
input en;
input [4:0] addr;
input [7:0] din;
output [7:0] dout;
wire [7:0] dout;

reg [7:0] mem [0:32-1];



always @(posedge clk) begin: SIMPLE_MEMORY_WRITE
    if (en) begin
        mem[addr] <= din;
    end
end



assign dout = mem[addr];

endmodule

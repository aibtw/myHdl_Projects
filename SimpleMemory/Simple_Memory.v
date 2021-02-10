// File: Simple_Memory.v
// Generated by MyHDL 0.11
// Date: Wed Feb 10 10:35:49 2021


`timescale 1ns/10ps

module Simple_Memory (
    clk,
    rst,
    en,
    addr,
    din,
    dout
);
// A simple memory made of 32 8-bit registers.
// :param clk: Clock signal
// :param rst: Reset signal
// :param en: Write enable signal
// :param addr: Address to write or read from
// :param din: Data input
// :param dout: Data output

input clk;
input rst;
input en;
input [4:0] addr;
input [7:0] din;
output [7:0] dout;
wire [7:0] dout;

reg [7:0] mem [0:32-1];



always @(posedge clk, negedge rst) begin: SIMPLE_MEMORY_WRITE
    if (rst == 0) begin
        mem[0] <= 0;
        mem[1] <= 0;
        mem[2] <= 0;
        mem[3] <= 0;
        mem[4] <= 0;
        mem[5] <= 0;
        mem[6] <= 0;
        mem[7] <= 0;
        mem[8] <= 0;
        mem[9] <= 0;
        mem[10] <= 0;
        mem[11] <= 0;
        mem[12] <= 0;
        mem[13] <= 0;
        mem[14] <= 0;
        mem[15] <= 0;
        mem[16] <= 0;
        mem[17] <= 0;
        mem[18] <= 0;
        mem[19] <= 0;
        mem[20] <= 0;
        mem[21] <= 0;
        mem[22] <= 0;
        mem[23] <= 0;
        mem[24] <= 0;
        mem[25] <= 0;
        mem[26] <= 0;
        mem[27] <= 0;
        mem[28] <= 0;
        mem[29] <= 0;
        mem[30] <= 0;
        mem[31] <= 0;
    end
    else begin
        if (en) begin
            mem[addr] <= din;
        end
    end
end



assign dout = mem[addr];

endmodule

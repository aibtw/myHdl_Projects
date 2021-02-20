// File: decoder_4bit.v
// Generated by MyHDL 0.11
// Date: Sat Feb 20 15:11:21 2021


`timescale 1ns/10ps

module decoder_4bit (
    inpu,
    out,
    enable
);


input [3:0] inpu;
output [15:0] out;
reg [15:0] out;
input enable;




always @(enable, inpu) begin: DECODER_4BIT_LOGIC
    if (enable) begin
        out = (2 ** inpu);
    end
    else begin
        out = 0;
    end
end

endmodule

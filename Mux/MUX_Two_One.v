// File: MUX_Two_One.v
// Generated by MyHDL 0.11
// Date: Mon Feb 15 16:32:15 2021


`timescale 1ns/10ps

module MUX_Two_One (
    z,
    a,
    b,
    sel
);


output [7:0] z;
reg [7:0] z;
input [7:0] a;
input [7:0] b;
input [1:0] sel;




always @(sel, a, b) begin: MUX_TWO_ONE_COMBLOGIC
    if ((sel == 1)) begin
        z = a;
    end
    else begin
        z = b;
    end
end

endmodule

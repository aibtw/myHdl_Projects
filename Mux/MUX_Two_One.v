// File: MUX_Two_One.v
// Generated by MyHDL 0.11
// Date: Thu Feb 11 21:38:27 2021


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
input [2:0] sel;




always @(b, sel, a) begin: MUX_TWO_ONE_COMBLOGIC
    case (sel)
        'h1: begin
            z = a;
        end
        'h0: begin
            z = b;
        end
    endcase
end

endmodule

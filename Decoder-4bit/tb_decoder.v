//Test 4-bit decoder

module tb_decoder;

reg [3:0] in;
reg en;
wire [15:0] out;

decoder_4bit DEC(in, out, en);

initial begin
	in = 0;
	en = 1;#50;
	repeat(15) begin
		in = in + 1; #50;
	end
end
endmodule
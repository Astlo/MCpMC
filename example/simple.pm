dtmc

param int p;
module toy


s : [0..4];

[] s=0 -> 0.2 : (s'=3) + p : (s'=1) + (1-p-0.2) : (s'=2);

endmodule


rewards
[]s=2 : 1;
endrewards

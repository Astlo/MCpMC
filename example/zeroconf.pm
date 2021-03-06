// Model taken from Daws04
// This version by Ernst Moritz Hahn (emh@cs.uni-sb.de)

probabilistic

param double p;
param double q;
const int n = 140;

module main
  s: [-2..n+1];

  [b] (s=-1) -> (s'=-2);
  [a] (s=0) -> 1-q : (s'=-1) + q : (s'=1);
  [a] (s>0) & (s<n+1) -> 1-p : (s'=0) + p : (s'=s+1);

endmodule

init
  s = 0
endinit

rewards
 [a] true : 1;
 [b] true : n-1;
endrewards

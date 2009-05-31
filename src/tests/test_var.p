program test_var; 
var 
y,z : real;  
a : char;
b : boolean;
c : integer;

procedure ScopeInner;
var K : char;
begin
	writeln(a);
end;

procedure Sco;
var P : integer;
Q, z : real; 
begin
	P := 10;
	z := 4.4;
	Q := 2.2 * z;	
	writeln(P);
end;

begin 
   	z := 2.2;
  	 y := 1.3 + z;
  	 a := 'y';
  	 b := faLse;
 	  c := 2 + 5*2 + 4 mod 7 div 6;
  	 write('O mod z e: ');
  	 writeln(y);
  	 writeln(a);
  	 writeln(b);
  	 write(c);

end.

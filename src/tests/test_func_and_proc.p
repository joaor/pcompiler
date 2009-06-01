program test3;
var A : integer;

procedure ScopeInner;
var P : integer;
begin
	A := 10;
	writeln(A);
end;

function Summation (num : real) : real;
var f : real;
begin
		writeln(P);
		f := num;
  	if num = 1 then
    		Summation := 1.1
  	else
    		f := Summation(num)
end;

begin
  	A := 20;
  	writeln(A);
  	Summation(2.3);
  	writeln(A);
  		begin
  			write(A);
  			write(P);
  		end;
end.

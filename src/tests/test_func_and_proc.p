program test3;
var A : integer;

procedure ScopeInner;
var P : integer;
begin
	A := 10;
	writeln(A);
end;

function Summation (num : integer) : integer;
var f : integer;
begin
		writeln(P);
  	if num = 1 then
    		Summation := 1
  	else
    		Summation := Summation(num-1) + num
end;

begin
  	A := 20;
  	writeln(A);
  	ScopeInner;
  	writeln(A);
  		begin
  			write(A);
  			write(P);
  		end;
end.

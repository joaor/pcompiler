program test3;
var A,a : integer;

procedure ScopeInner;
var P,p,p,p : integer;
begin
	A := 10;
	writeln(A);
end;

function Summation (num : integer) : integer;
var f ,F : integer;
begin
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
end.

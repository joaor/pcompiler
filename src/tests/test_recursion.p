program test3;
var A : integer;

function Summation(num : integer) : integer;
var f,m : integer;
begin
	f := num - 1;
	writeln(f);
  	if f = 1 then
		begin
    			Summation := 1;
		end
  	else
		begin
			m := Summation(f);
    			Summation := m;
		end
end;

begin
  	A := Summation(20);
  	writeln(A);
end.

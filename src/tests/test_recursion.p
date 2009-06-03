program test3;
var A : integer;

function Summation(num : integer) : integer;
var f,m,a,ola,count : integer;
begin
	f := num - 1;
	writeln(f);
	while a < 6 do
	  	begin
			ola := 1;
	    		for count := 5 downto 1 do	
				begin
		  			ola := ola + count;
					writeln (ola);
				end;
			writeln('Vou incrementar');
			a := a +1;
			writeln(a);
	  	end;
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

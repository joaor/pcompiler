program test_var; 
var 
c,a : integer;

begin
  	c := 20;

	a := 1;
	while a < 6 do
	  	begin
	    		writeln (a);
	   		 a := a + 1
	  	end;

	if not ((c <> 20) or (c = 20)) then
		begin
			writeln('PI');
			writeln('PI');
		end;
	if c >= 20 then 
		begin
			if c = 21 then 
				begin
					if c = 20 then 
					begin
						writeln('P9');
						writeln('P9');
					end
				end
			else
				begin
					writeln('Pyy');
					writeln('Pyy');
				end
		end
	else
		begin
			writeln('P00');
			writeln('P00');
		end
end.


program test_var; 
var 
c : integer;

begin
  	c := 20;
	if not ((c <> 20) or (c = 20)) then
		begin
			writeln('PI');
			writeln('PI');
		end;
	if c = 20 then 
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
					writeln('P00');
					writeln('P00');
				end
		end
	else
		begin
			writeln('P00');
			writeln('P00');
		end
end.


program test_var; 
var 
c,a,sum,count : integer;

begin
  	
	sum := 1;
	for count := 1 to 5 do	
		begin
  			sum := sum + count;
			writeln (sum);
		end;
	writeln ('passou para o while');
	a := 1;
	while a < 6 do
	  	begin
	    		while a < 6 do
			  	begin
			    		writeln (a);
			   		 a := a + 1
			  	end;
			writeln ('vou a casa');
	  	end;

	if not ((c <> 20) or (c = 20)) then
		begin
			writeln('PI');
			writeln('PI');
		end;

	c := 20;
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


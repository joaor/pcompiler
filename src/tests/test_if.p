program test_var; 
var 
c,a,sum,count1,count2,ola : integer;

begin
  	
	sum := 1;
	for count1 := 1 to 5 do	
		begin
  			sum := sum + count1;
			writeln (sum);
			ola := 1;
			for count2 := 5 downto 1 do	
				begin
		  			ola := ola + count2;
					writeln (ola);
				end;
		end;
end.


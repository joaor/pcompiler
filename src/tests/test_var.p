program test_var; 
var 
y,z : real;  
a : char;
b : boolean;
c : integer;



function Add(i, j:Integer): Integer;
begin
   	Add := i + j;
end;

function Sub : real;
begin
   	Sub := 3.9 - 2.2;
end;


begin 

	c := Add(3,2);
	writeln(c);
	z := Sub;
	writeln(z);
end.

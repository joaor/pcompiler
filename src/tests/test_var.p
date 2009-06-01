program test_var; 
var 
y,z : real;  
a : char;
b : boolean;
c,v : integer;



function Add(i, j:Integer): Integer;
begin
	writeln('ola');
   	Add := i + j;
	c := i + j;
	writeln(c);
end;

function Sub : real;
begin
	writeln('ole');
   	Sub := 3.9 - 2.2;
end;


begin 


	v := Add(3,2);
	z := Sub;
end.

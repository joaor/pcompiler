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
end;

function Sub : real;
begin
	writeln('ole');
	c := Add(6,7);
		begin
			Sub := 3.9;
		end;
   	writeln(c);
end;

begin
  	c := 20;
  	writeln(c);
  		begin
  			c := 6;
			v := Add(3,c);
			writeln(v);
			z := Sub;
			writeln(z);
  		end;
end.
yacc: Warning. Token 'CONST' defined, but not used.
yacc: Warning. Token 'EXP' defined, but not used.
yacc: Warning. Token 'COMMENT' defined, but not used.
yacc: Warning. Token 'IN' defined, but not used.
yacc: Warning. Token 'NIL' defined, but not used.
yacc: Warning. Token 'BOOLEAN' defined, but not used.
yacc: Warning. Token 'TYPE' defined, but not used.


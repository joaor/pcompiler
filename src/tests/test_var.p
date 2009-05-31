program test_var; 
var 
y,z : real;  
a : char;
b : boolean;
c : integer;

procedure ScopeInner;
begin
	writeln(a);
end;

procedure Sco;
var Y : integer;
begin
	Y := 10;
	writeln(Y);
end;

begin 
   z := 2.2;
   y := 1.3 + z;
   a := 'y';
   b := faLse;
   c := 2 + 5*2 + 4 mod 7 div 6;
   write('O mod z e: ');
   writeln(y);
   writeln(a);
   writeln(b);
   write(c);

end.

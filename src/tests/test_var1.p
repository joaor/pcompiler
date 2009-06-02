program test_var; 
var 
y,z : real;  
a : char;
b : boolean;
c : integer;

procedure ScopeInner2(s: real; i: integer);
var K : char;
begin
	writeln(i);
end;

procedure ScopeInner(s: real; i: integer);
var K : char;
begin
	writeln(i);
	i := i +1;
	ScopeInner2(s,i);
end;

function Add(i, j:Integer): Integer;
begin
   	Add := i + j;
	ScopeInner2(2.2,j);
end;

procedure Sco;
var P : integer;
Q,z: real; 
begin
	P := 10 + c;
	z := 4.4;
	Q := 2.2 * z;	
	writeln(P);
	P := Add(P,1);
	ScopeInner(2.3,P);
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
  	writeln(c);
	Sco;
	ScopeInner(2.3,c);
	c := c +1;
	ScopeInner(5.7,c);
	c := Add(1,2);
	writeln(c);
end.

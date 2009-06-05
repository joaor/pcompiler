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
	writeln(c)
end;

procedure Sco;
var P,sum,count1,count2,ola : integer;
Q,z: real; 
begin
	P := 10 + c;
	z := 4.4;
	Q := 2.2 * z;	
	writeln(P);
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

program testBigMod; 
var 
	b,m,p,r : Integer; 
 
function square(n : Integer) : Integer; 
begin 
   square := n*n; 
end; 
 
function bigMod( b, p, m : Integer ) : Integer; 
var 
	a,c,d : Integer; 
begin 
	if p = 0 then begin  
		bigMod := 1;  
	end 
	else begin 
		if p MOD 2 = 0 then begin 
			a := p / 2;
			c := bigMod(b,a,m);
			d := square(c);
			bigMod :=  d MOD m; 
		end else begin 
			a := p-1;
			c := bigMod(b,a,m);
			bigMod := ((b MOD m) * c) MOD m;  
		end; 
	end; 
end; 
 
begin 
		b := 2374859;
		p := 3029382;
		m := 36123; 
		r := bigMod(b,p,m);
		writeln(r); 
 
end. 

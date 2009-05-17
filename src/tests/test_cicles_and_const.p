program test2; 
const a = 5; 
b= 10;
 
var j : real; 
i : integer;
 
begin 
j := 1 * 2; 
i := j * (1 + 2);
 
if 1 > 2 then 
	i := i + 1 
else 
	i := i * 2;
	 
while i < 10 do
	i := i + i;
 
repeat i := i - 1 until 
	i < 0;
 
for i := 1 to 10 do 
	j := j + 2; 
end.

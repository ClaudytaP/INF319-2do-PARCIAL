getnum :: IO Double
getnum = do
s <- getLine
return (read s)

main = do
	putStr("Calculadora en Haskell\n")
	putStr("")
	putStr("el número 1 es:\n")
	num1 <- getnum
	putStr("el número 2 es:\n")
	num2 <- getnum
	
	putStr("Seleccione la operación a realizar: \n")
	putStr("1.Suma\n2. Resta\n3. Multiplica\n4. Divide")
	opc <- getnum
	let suma=[c+d | c<- [num1], d <-[num2]]
	let resta=[c-d | c<- [num1], d <-[num2]]
	let multiplica=[c*d | c<- [num1], d <-[num2]]
	let divide=[c/d | c<- [num1], d <-[num2]]
	let resultado = if opc==1 then suma
			   else if opc==2 then resta
			   else if opc==3 then multiplica
			   else if opc==4 then divide else {}
	
	if(opc == 1 || opc == 2 || opc == 3 ||opc == 4)
	then putStr("El resultado es:" ++show(resultado)++"\n")
	else putStr("Opción no válida...\n")
	putStr("\n")
	main
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="ISO-8859-1">
<title>Insert title here</title>
</head>
<body>
<%
int num1 = 0;
int num2 =1;
int temp;
int limite = 50;
out.println(num1);
out.println(num2);

while(num2+num1 <= limite){
	temp = num1;
	temp = num2;
	num2 = temp +num1;
	out.println(num2);
}

%>
</body>
</html>
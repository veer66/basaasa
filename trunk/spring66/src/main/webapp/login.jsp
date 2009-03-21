<%--
    Document   : hello
    Created on : Feb 4, 2009, 11:36:47 AM
    Author     : TwinP
--%>

<%@page contentType="text/html" pageEncoding="utf-8"%>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN"
   "http://www.w3.org/TR/html4/loose.dtd">
<%
	String result;
	String loginUsername = request.getParameter("loginUsername");
	if (null != loginUsername && loginUsername.length() > 0) {
		if (loginUsername.equals("f"))
			result = "{success:true}";
		else
			result = "{success:false,errors:{reason:'Login failed.Try again'}}";

	} else {
		result = "{success:false,errors:{reason:'Login failed.Try again'}}";
	}
%>
<%=result%>
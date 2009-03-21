<%@ page language="java" contentType="text/html; charset=utf-8" %>
<%@ taglib uri="http://www.springframework.org/tags" prefix="spring" %>
<%@ taglib prefix="fmt" uri="http://java.sun.com/jsp/jstl/fmt" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>

<html>
    <body>
        <h2>Hello World!vvvv</h2>
        <c:forEach var="usr" items="${pettypeList}">
            <c:out value="${usr.name}"/>
        </c:forEach>
    </body>
</html>
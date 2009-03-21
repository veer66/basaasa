package com.spring66.training.dao.generic.finder.impl;

import com.spring66.training.dao.generic.finder.FinderArgumentTypeFactory;
import java.util.Properties;

import org.hibernate.type.Type;
import org.hibernate.type.TypeFactory;

/**
 * Maps Enums to a custom Hibernate user type
 */
public class SimpleFinderArgumentTypeFactory implements FinderArgumentTypeFactory {

    public Type getArgumentType(Object arg) {
//        if(arg instanceof Enum)
//        {
//            return getEnumType(arg.getClass());
//        }
//        else
//        {
        return null;
//        }
    }

//    private Type getEnumType(Class<? extends Object> argClass)
//    {
//        Properties p = new Properties();
//        p.setProperty("enumClassName", argClass.getName());
//        Type enumType = TypeFactory.heuristicType("org.hibernate.demo.EnumUserType", p);
//        return enumType;
//    }
}

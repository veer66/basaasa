package com.spring66.tutorial;


import com.spring66.training.entity.Vet;
import java.util.Date;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.hibernate.Hibernate;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.AnnotationConfiguration;
import org.hibernate.cfg.Environment;
import org.hibernate.dialect.MySQLDialect;

/**
 * Unit test for simple App.
 */
public class AppTestVet
        extends TestCase {

    private static SessionFactory sessionFactory;

    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTestVet(String testName) {
        super(testName);
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(AppTestVet.class);
    }

    @Override
    protected void setUp() throws Exception {
        try {
            AnnotationConfiguration configuration =
                    new AnnotationConfiguration();
            configuration.setProperty(
                    Environment.DRIVER,
                    "com.mysql.jdbc.Driver");
            configuration.setProperty(
                    Environment.URL,
                    "jdbc:mysql://localhost:3306/dem");
            configuration.setProperty(
                    Environment.USER, "root");
            configuration.setProperty(
                    Environment.PASS, "password");
            configuration.setProperty(
                    Environment.DIALECT,
                    MySQLDialect.class.getName());
            configuration.setProperty(
                    Environment.SHOW_SQL, "true");
            configuration.setProperty(
                    Environment.HBM2DDL_AUTO, "create");
            configuration.addPackage("com.spring66.training.hibernate");
            configuration.addAnnotatedClass(Vet.class);
            /*configuration.addAnnotatedClass(Visit.class);
            configuration.addAnnotatedClass(Owner.class);
            configuration.addAnnotatedClass(PetType.class);*/
            sessionFactory =
                    configuration.buildSessionFactory();
        } catch (Throwable ex) {
            // Log exception!
            ex.printStackTrace();
            throw new ExceptionInInitializerError(ex);
        }
    }

    /**
     * Rigourous Test :-)
     */
    public void testApp() {
        Session session = sessionFactory.openSession();
        Transaction tx = session.beginTransaction();
        assertNotNull(sessionFactory);
        Vet vet = new Vet();
        vet.setFirstName("firstName");
        vet.setLastName("lastname");
        session.persist(vet);
        tx.commit();
        session.close();
    }
}

package com.spring66.training;

import com.spring66.training.entity.Pet;
import com.spring66.training.entity.Visit;
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
public class AppTestVisit
        extends TestCase {

    private static SessionFactory sessionFactory;

    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public AppTestVisit(String testName) {
        super(testName);
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(AppTestVisit.class);
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
            //configuration.addAnnotatedClass(Troop.class);
            //configuration.addAnnotatedClass(Soldier.class);
            configuration.addAnnotatedClass(Pet.class);
            configuration.addAnnotatedClass(Visit.class);
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
        Pet t = new Pet();
		t.setName( "Final cut" );
		Visit vandamme = new Visit();
		vandamme.setName( "JC Vandamme" );
		t.addVisit(vandamme);
		Visit rambo = new Visit();
		rambo.setName( "Rambo" );
		t.addVisit( rambo );
		session.persist( t );
        tx.commit();
		session.close();

        session = sessionFactory.openSession();
		tx = session.beginTransaction();
		t = (Pet) session.get( Pet.class, t.getId() );
		assertNotNull( t.getVisits() );
		assertFalse( Hibernate.isInitialized( t.getVisits() ) );
		assertEquals( 2, t.getVisits().size() );
		assertEquals( rambo.getName(), t.getVisits().iterator().next().getName() );
		tx.commit();
		session.close();

    }
}

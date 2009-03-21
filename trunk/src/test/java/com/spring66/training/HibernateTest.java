package com.spring66.training;

import com.spring66.training.hibernate.Group;
import com.spring66.training.hibernate.Permission;
import java.util.ArrayList;
import java.util.Collection;
import java.util.Date;
import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.hibernate.cfg.AnnotationConfiguration;
import org.hibernate.cfg.Environment;
import org.hibernate.dialect.MySQLDialect;

/**
 * Unit test for simple App.
 */
public class HibernateTest
        extends TestCase {

    private static SessionFactory sessionFactory;

    /**
     * Create the test case
     *
     * @param testName name of the test case
     */
    public HibernateTest(String testName) {
        super(testName);
    }

    /**
     * @return the suite of tests being tested
     */
    public static Test suite() {
        return new TestSuite(HibernateTest.class);
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
                    "jdbc:mysql://localhost:3306/hibernate");
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
            configuration.addPackage("com.spring66.training.entity");
            //configuration.addAnnotatedClass(BaseEntity.class);
            //configuration.addAnnotatedClass(NamedEntity.class);
            /*configuration.addAnnotatedClass(PetType.class);
            configuration.addAnnotatedClass(Person.class);
            configuration.addAnnotatedClass(Specialty.class);
            configuration.addAnnotatedClass(Visit.class);
            configuration.addAnnotatedClass(Pet.class);*/
            configuration.addAnnotatedClass(Group.class);
            configuration.addAnnotatedClass(Permission.class);
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
        Session s = sessionFactory.openSession();
        assertNotNull(sessionFactory);
        Transaction tx = s.beginTransaction();


		//s.enableFilter( "Groupfilter" );
		Permission readAccess = new Permission();
		readAccess.setPermission( "read" );
		readAccess.setExpirationDate( new Date() );
		Permission writeAccess = new Permission();
		writeAccess.setPermission( "write" );
		writeAccess.setExpirationDate( new Date( new Date().getTime() - 10*60*1000 ) );
		Collection<Permission> coll = new ArrayList<Permission>( 2 );
		coll.add( readAccess );
		coll.add( writeAccess );
		Group group = new Group();
		group.setId( new Integer( 1 ) );
		group.setPermissions( coll );
		s.getTransaction().begin();
		s.persist( group );
		s.flush();
		s.clear();
		group = (Group) s.get( Group.class, group.getId() );
		s.createQuery( "select g from Group g join fetch g.permissions").list();
		assertNotNull(group.getPermissions().iterator().next().getPermission() );
		s.getTransaction().commit();
		s.close();

  
       // Pet pp = (Pet) session.load(Pet.class, pet.getId());
        //System.out.println("Pet has ->" + pp.getVisits().size());
       // assertEquals(2, pp.getVisits().size());
        //session.getTransaction().commit();

    //assertEquals(1, add.getId().intValue());
    }
}

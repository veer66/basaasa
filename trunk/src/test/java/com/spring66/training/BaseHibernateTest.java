//$Id: TestCase.java 15025 2008-08-11 09:14:39Z hardy.ferentschik $
package com.spring66.training;

import junit.framework.Test;
import junit.framework.TestCase;
import junit.framework.TestSuite;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.cfg.AnnotationConfiguration;
import org.hibernate.cfg.Configuration;
import org.hibernate.cfg.Environment;
import org.hibernate.dialect.MySQLDialect;

/**
 * A base class for all tests.
 * 
 * @author Emmnauel Bernand
 * @author Hardy Ferentschik
 */
public abstract class BaseHibernateTest extends TestCase {

//	public static final Logger log = LoggerFactory.getLogger(TestCase.class);
    private static SessionFactory sessionFactory;
    private static AnnotationConfiguration cfg;
    private Session session;

    public static Test suite() {
        return new TestSuite(BaseHibernateTest.class);
    }

    public BaseHibernateTest(String testName) {
        super(testName);
    }

    @Override
    protected void setUp() throws Exception {
        /*try {
        Configuration configuration =
        new Configuration();
        configuration.setProperty(
        Environment.DRIVER,
        "org.hsqldb.jdbcDriver");
        configuration.setProperty(
        Environment.URL,
        "jdbc:hsqldb:mem:ProductDAOTest");
        configuration.setProperty(
        Environment.USER, "sa");
        configuration.setProperty(
        Environment.DIALECT,
        MySQLDialect.class.getName());
        configuration.setProperty(
        Environment.SHOW_SQL, "true");
        configuration.setProperty(
        Environment.HBM2DDL_AUTO, "create-drop");
        //configuration.addClass(Product.class);
        //configuration.addClass(Component.class);

        sessionFactory =
        configuration.buildSessionFactory();
        } catch (Throwable ex) {
        // Log exception!
        throw new ExceptionInInitializerError(ex);
        }*/
    }

    public void testStoreRetrieve() {
        assertNotNull(this.sessionFactory);
    }
}

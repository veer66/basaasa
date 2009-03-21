/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.dao.hibernate;

import com.spring66.training.dao.PetTypeDao;
import com.spring66.training.entity.PetType;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.test.AbstractDependencyInjectionSpringContextTests;

/**
 *
 * @author TwinP
 */
public class PetTypeDaoHibernateTest extends AbstractDependencyInjectionSpringContextTests {
    protected final Log log = LogFactory.getLog(getClass());
    private PetTypeDao pettypeDao;
    //private Clinic clinic;
    @Override
    protected String[] getConfigLocations() {
               setAutowireMode(AUTOWIRE_BY_NAME);
        return new String[] {
                "classpath:/applicationContext.xml",
                "classpath*:/applicationContext.xml" // for modular projects
                //"classpath:**/applicationContext*.xml" // for web projects
            };
    }

    /**
     * Test of create method, of class PetTypeDaoHibernate.
     */
    public void testCreate() {
        PetType pt = new PetType();
        pt.setName("Cat");
        pettypeDao.create(pt);
        //fail("You are fail to test");
    }

    /**
     * Test of read method, of class PetTypeDaoHibernate.
     */
    public void testRead() {
    }

    /**
     * Test of update method, of class PetTypeDaoHibernate.
     */
    public void testUpdate() {
    }

    /**
     * Test of delete method, of class PetTypeDaoHibernate.
     */
    public void testDelete() {
    }

    /**
     * @return the petTypeDao
     */
    public PetTypeDao getPettypeDao() {
        return pettypeDao;
    }

    /**
     * @param petTypeDao the petTypeDao to set
     */
    public void setPettypeDao(PetTypeDao petTypeDao) {
        this.pettypeDao = petTypeDao;
    }

}

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.dao.hibernate;

import com.spring66.training.dao.OwnerDao;
import com.spring66.training.entity.Owner;
import java.util.Collection;
import java.util.List;


import org.hibernate.SessionFactory;

/**
 *
 * @author TwinP
 */
public class OwnerDaoHibernate implements OwnerDao {

    private SessionFactory sessionFactory;

    @Override
    public void create(Owner own) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public Owner loadOwner(Integer pk) {
        return (Owner) sessionFactory.getCurrentSession().load(Owner.class, pk);
    }

    @Override
    public void update(Owner own) {
        sessionFactory.getCurrentSession().saveOrUpdate(own);
    }

    @Override
    public void delete(Owner own) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public List<Owner> readAll() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public Collection<Owner> findOwner(String lastName) {
        return sessionFactory.getCurrentSession().createQuery("from Owner owner where owner.lastName like ?").setParameter(0, lastName + "%").list();
    }

    @Override
    public void storeOwner(Owner own) {
        sessionFactory.getCurrentSession().saveOrUpdate(own);
    }

    public void setSessionFactory(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }
}

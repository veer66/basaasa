/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.dao.hibernate;

import com.spring66.training.dao.PetDao;
import com.spring66.training.entity.Pet;
import java.util.List;
import org.hibernate.Session;
import org.hibernate.SessionFactory;
import org.hibernate.Transaction;
import org.springframework.transaction.annotation.Transactional;

/**
 *
 * @author TwinP
 */
public class PetDaoHibernate implements PetDao {

    private SessionFactory sessionFactory;

    public void setSessionFactory(SessionFactory sessionFactory) {
        this.sessionFactory = sessionFactory;
    }

    @Override
    @Transactional
    public void create(Pet pet) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    @Transactional
    public Pet loadPet(final Integer pk) {
        /*Session session = sessionFactory.openSession();
        try {
        return (Pet) session.get(Pet.class, pk);
        } finally {
        session.close();
        }*/
        return (Pet)sessionFactory.getCurrentSession().load(Pet.class, pk);
    }

    @Override
    @Transactional
    public void update(Pet pet) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    @Transactional
    public void delete(Pet pet) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    @Transactional
    public List<Pet> readAll() {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    @Transactional
    public void storePet(Pet pet) {
        /*Session session = sessionFactory.openSession();
        Transaction tx = (Transaction) session.getTransaction();
        try {
        tx.begin();
        session.saveOrUpdate(pet);
        tx.commit();
        } catch (RuntimeException e) {
        tx.rollback();
        throw e;
        } finally {
        session.close();
        }*/
        sessionFactory.getCurrentSession().saveOrUpdate(pet);
    }
}

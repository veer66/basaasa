/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.dao.hibernate;

import com.spring66.training.dao.VetDao;
import com.spring66.training.entity.Vet;
import java.util.List;
import org.springframework.orm.hibernate3.support.HibernateDaoSupport;

/**
 *
 * @author TwinP
 */
public class VetDaoHibernate extends HibernateDaoSupport implements VetDao{

    @Override
    public void create(Vet vt) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public Vet read(Integer pk) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public List<Vet> readAll() {
        return getHibernateTemplate().find("from Vet");
    }

    @Override
    public void update(Vet vt) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

    @Override
    public void delete(Vet vt) {
        throw new UnsupportedOperationException("Not supported yet.");
    }

}

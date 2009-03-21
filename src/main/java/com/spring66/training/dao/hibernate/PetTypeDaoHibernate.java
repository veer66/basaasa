/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.dao.hibernate;

import com.spring66.training.dao.PetTypeDao;
import com.spring66.training.entity.PetType;
import java.util.List;
import org.springframework.orm.hibernate3.support.HibernateDaoSupport;

/**
 *
 * @author TwinP
 */
public class PetTypeDaoHibernate extends HibernateDaoSupport implements PetTypeDao{

    @Override
    public void create(PetType pt) {
        getHibernateTemplate().saveOrUpdate(pt);
    }

    @Override
    public PetType read(Integer pk) {
      return (PetType)getHibernateTemplate().get(PetType.class, pk);
    }

    @Override
    public void update(PetType pt) {
        getHibernateTemplate().update(pt);
    }

    @Override
    public void delete(PetType pt) {
        getHibernateTemplate().delete(pt);
    }

    public List<PetType> readAll(){
         return getHibernateTemplate().find("from PetType");
    }
}

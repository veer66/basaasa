/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.dao;

import com.spring66.training.entity.Visit;
import java.util.Collection;
import java.util.List;

/**
 *
 * @author TwinP
 */
public interface VisitDao {
    public void create(Visit visit);
    public void storeVisit(Visit visit);
    public Visit loadVisit(Integer pk);
    public void update(Visit visit);
    public void delete(Visit visit);
    public List<Visit> readAll();
    public Collection<Visit> findOwner(String name);
}

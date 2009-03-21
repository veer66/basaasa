/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.dao;

import com.spring66.training.entity.PetType;
import java.util.List;

/**
 *
 * @author TwinP
 */
public interface PetTypeDao {
    public void create(PetType pt);
    public PetType read(Integer pk);
    public void update(PetType pt);
    public void delete(PetType pt);
    public List<PetType> readAll();
}

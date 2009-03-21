/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.dao;

import com.spring66.training.entity.Pet;
import java.util.List;

/**
 *
 * @author TwinP
 */
public interface PetDao {
    public void create(Pet pet);
    public Pet loadPet(Integer pk);
    public void update(Pet pet);
    public void delete(Pet pet);
    public List<Pet> readAll();
    public void storePet(Pet pet);
}

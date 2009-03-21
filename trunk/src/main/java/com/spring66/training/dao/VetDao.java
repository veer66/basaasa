/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.dao;

import com.spring66.training.entity.Vet;
import java.util.List;

/**
 *
 * @author TwinP
 */
public interface VetDao {

    public void create(Vet vt);

    public Vet read(Integer pk);

    public List<Vet> readAll();

    public void update(Vet vt);

    public void delete(Vet vt);
}

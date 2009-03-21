/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.entity;

import javax.persistence.Entity;
import javax.persistence.Table;

/**
 *
 * @author TwinP
 */
@Entity
@Table(name="Specialties")
public class Specialty extends NamedEntity {
    /*private String name;


    @Id
    public String getName() {
    return name;
    }

    public void setName(String name) {
    this.name = name;
    }*/

}

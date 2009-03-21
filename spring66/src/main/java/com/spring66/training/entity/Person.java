/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.entity;

import javax.persistence.Entity;
import javax.persistence.MappedSuperclass;

/**
 *
 * @author TwinP
 */
@MappedSuperclass
public class Person extends BaseEntity {

    private String firstName;
    private String lastName;

    public String getFirstName() {
        return this.firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return this.lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }
}

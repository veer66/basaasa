/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.entity;

import javax.persistence.MappedSuperclass;

/**
 *
 * @author TwinP
 */
@MappedSuperclass
public class NamedEntity extends BaseEntity {

    protected String name;

    public void setName(String name) {
        this.name = name;
    }

    public String getName() {
        return this.name;
    }

    @Override
    public String toString() {
        return this.getName();
    }

    @Override
    public int hashCode() {
        return name.hashCode();
    }
}

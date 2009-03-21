/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.entity;

import java.io.Serializable;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.MappedSuperclass;
import javax.persistence.Transient;

/**
 *
 * @author TwinP
 */
@MappedSuperclass
public class BaseEntity implements Serializable {

    protected Integer id;

    public void setId(Integer id) {
        this.id = id;
    }

    @Id
    @GeneratedValue
    public Integer getId() {
        return id;
    }

    @Transient
    public boolean isNew() {
        return (this.id == null);
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        BaseEntity be = (BaseEntity)o;
        if (!id.equals(be.id)) {
            return false;
        }
        return true;
    }
}

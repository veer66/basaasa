/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.entity;

import com.spring66.training.entity.Pet;
import com.spring66.training.entity.BaseEntity;
import java.util.Date;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.Temporal;

/**
 * @author Emmanuel Bernard
 */
@Entity
public class Visit extends BaseEntity{
	//private Integer id;
	private String name;
	private Pet pet;
    private String description;
    private Date visitDate;


	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	@ManyToOne(fetch = FetchType.EAGER)
	@JoinColumn(name = "pet_fk")
	public Pet getPet() {
		return pet;
	}

	public void setPet(Pet pet) {
		this.pet = pet;
	}

    /**
     * @return the description
     */
    public String getDescription() {
        return description;
    }

    /**
     * @param description the description to set
     */
    public void setDescription(String description) {
        this.description = description;
    }

    /**
     * @return the visitDate
     */
    @Temporal(javax.persistence.TemporalType.DATE)
    public Date getVisitDate() {
        return visitDate;
    }

    /**
     * @param visitDate the visitDate to set
     */
    public void setVisitDate(Date visitDate) {
        this.visitDate = visitDate;
    }

    	public boolean equals(Object o) {
		if ( this == o ) return true;
		if ( !( o instanceof Visit ) ) return false;

		final Visit visit = (Visit) o;

		if ( !name.equals( visit.name ) ) return false;

		return true;
	}

	public int hashCode() {
        if (name == null) {
            return 1;
        } else {
            return name.hashCode();
        }
	}
}

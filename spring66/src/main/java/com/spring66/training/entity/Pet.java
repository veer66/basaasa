/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.entity;

import java.util.Date;
import java.util.HashSet;
import java.util.Set;
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.ManyToOne;
import javax.persistence.OneToMany;

import javax.persistence.OneToOne;
import javax.persistence.Table;
import javax.persistence.Temporal;
import org.hibernate.annotations.OnDelete;
import org.hibernate.annotations.OnDeleteAction;
import org.hibernate.annotations.OrderBy;

/**
 * Shows a default one to many
 *
 * @author Emmanuel Bernard
 */
@Entity
@Table(name = "pets")
public class Pet {

    private Integer id;
    private String name;
    private Date birthDate;
    private PetType type;
    private Set<Visit> visits;
    private Owner owner;

    @Id
    @GeneratedValue
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public void addVisit(Visit v) {
        if (getVisits() == null) {
            setVisits(new HashSet<Visit>());
        }
        getVisits().add(v);
        v.setPet(this);
    }

    /**
     * @return the visits
     */
    @OneToMany(mappedBy = "pet", cascade = {CascadeType.ALL}, fetch = FetchType.LAZY)
    @OrderBy(clause = "name desc")
    @org.hibernate.annotations.Cascade(org.hibernate.annotations.CascadeType.DELETE_ORPHAN)
    @OnDelete(action = OnDeleteAction.CASCADE)
    public Set<Visit> getVisits() {
        return visits;
    }

    /**
     * @param visits the visits to set
     */
    public void setVisits(Set<Visit> visits) {
        this.visits = visits;
    }

    /**
     * @return the petType
     */
    @OneToOne(cascade = CascadeType.ALL)
    @JoinColumn(name = "pettype_fk")
    public PetType getType() {
        return type;
    }

    /**
     * @param petType the petType to set
     */
    public void setType(PetType type) {
        this.type = type;
    }

    /**
     * @return the owner
     */
    @ManyToOne(fetch = FetchType.EAGER)
    @JoinColumn(name = "owner_fk")
    public Owner getOwner() {
        return owner;
    }

    /**
     * @param owner the owner to set
     */
    public void setOwner(Owner owner) {
        this.owner = owner;
    }

    public boolean equals(Object o) {
        if (this == o) {
            return true;
        }
        if (!(o instanceof Visit)) {
            return false;
        }

        final Pet pet = (Pet) o;

        if (!name.equals(pet.name)) {
            return false;
        }

        return true;
    }

    public int hashCode() {
        if (name == null) {
            return 1;
        } else {
            return name.hashCode();
        }
    }

    /**
     * @return the birthDate
     */
    @Temporal(javax.persistence.TemporalType.DATE)
    public Date getBirthDate() {
        return birthDate;
    }

    /**
     * @param birthDate the birthDate to set
     */
    public void setBirthDate(Date birthDate) {
        this.birthDate = birthDate;
    }
}


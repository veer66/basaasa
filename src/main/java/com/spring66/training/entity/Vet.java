/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.entity;

import java.util.ArrayList;
import java.util.Collection;
import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Set;
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.FetchType;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.OrderBy;
import javax.persistence.Table;
import javax.persistence.Transient;
import javax.persistence.UniqueConstraint;
import org.springframework.beans.support.MutableSortDefinition;
import org.springframework.beans.support.PropertyComparator;

/**
 *
 * @author TwinP
 */
@Entity
@Table(name="Vets")
public class Vet extends Person {

    private Collection<Specialty> specialties;

    /**
     * @return the specialties
     */
    @ManyToMany(cascade = CascadeType.PERSIST, fetch = FetchType.LAZY)
    @JoinTable(name = "VETS_SPECIALTIES",
    uniqueConstraints = @UniqueConstraint(columnNames = {"vet_id", "name"}),
    joinColumns = @JoinColumn(name = "vet_id", referencedColumnName = "id"),
    inverseJoinColumns = @JoinColumn(name = "name", referencedColumnName = "id"))
    @OrderBy("name")
    public Collection<Specialty> getSpecialties() {
        List<Specialty> sortedSpecs = new ArrayList<Specialty>(getSpecialtiesInternal());
        PropertyComparator.sort(sortedSpecs, new MutableSortDefinition("name", true, true));
        return Collections.unmodifiableList(sortedSpecs);
    }

    /**
     * @param specialties the specialties to set
     */
    public void setSpecialties(Collection<Specialty> specialties) {
        this.specialties = specialties;
    }

    @Transient
    protected Collection<Specialty> getSpecialtiesInternal() {
        if (this.specialties == null) {
            this.specialties = new HashSet<Specialty>();
        }
        return this.specialties;
    }

    @Transient
    public int getNrOfSpecialties() {
        return getSpecialtiesInternal().size();
    }

    public void addSpecialty(Specialty specialty) {
        getSpecialtiesInternal().add(specialty);
    }
}

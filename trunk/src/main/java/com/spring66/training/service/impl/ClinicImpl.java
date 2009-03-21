/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.service.impl;

import com.spring66.training.dao.OwnerDao;
import com.spring66.training.dao.PetDao;
import com.spring66.training.service.Clinic;
import com.spring66.training.dao.PetTypeDao;
import com.spring66.training.dao.VetDao;
import com.spring66.training.dao.VisitDao;
import com.spring66.training.entity.Owner;
import com.spring66.training.entity.Pet;
import com.spring66.training.entity.PetType;
import com.spring66.training.entity.Vet;
import com.spring66.training.entity.Visit;
import java.util.Collection;
import org.springframework.dao.DataAccessException;

/**
 *
 * @author TwinP
 */
public class ClinicImpl implements Clinic {

    private OwnerDao ownerDao;
    private PetDao petDao;
    private PetTypeDao pettypeDao;
    private VetDao vetDao;
    private VisitDao visitDao;

    //@Transactional(readOnly = true)
    @Override
    public Collection<Vet> getVets() throws DataAccessException {
        return getVetDao().readAll();
    }

    //@Transactional(readOnly = true)
    @Override
    public Collection<PetType> getPetTypes() throws DataAccessException {
        return pettypeDao.readAll();
    }

    //@Transactional(readOnly = true)
    @Override
    public Collection<Owner> findOwners(String lastName) throws DataAccessException {
        return ownerDao.findOwner(lastName);
    }

    //@Transactional(readOnly = true)
    @Override
    public Owner loadOwner(int id) throws DataAccessException {
        return ownerDao.loadOwner(id);
    }

    //@Transactional(readOnly = true)
    @Override
    public Pet loadPet(int id) throws DataAccessException {
        return petDao.loadPet(id);
    }

    @Override
    //@Transactional(readOnly = false, propagation = Propagation.REQUIRES_NEW)
    public void storeOwner(Owner owner) throws DataAccessException {
        ownerDao.storeOwner(owner);
    }

    @Override
    //@Transactional(readOnly = false, propagation = Propagation.REQUIRES_NEW)
    public void storePet(Pet pet) throws DataAccessException {
        petDao.storePet(pet);
    }

    @Override
    //@Transactional(readOnly = false, propagation = Propagation.REQUIRES_NEW)
    public void storeVisit(Visit visit) throws DataAccessException {
        visitDao.storeVisit(visit);
    }

    /**
     * @return the pettypeDao
     */
    public PetTypeDao getPettypeDao() {
        return pettypeDao;
    }

    /**
     * @param pettypeDao the pettypeDao to set
     */
    public void setPettypeDao(PetTypeDao pettypeDao) {
        this.pettypeDao = pettypeDao;
    }

    /**
     * @return the vetDao
     */
    public VetDao getVetDao() {
        return vetDao;
    }

    /**
     * @param vetDao the vetDao to set
     */
    public void setVetDao(VetDao vetDao) {
        this.vetDao = vetDao;
    }

    /**
     * @return the ownerDao
     */
    public OwnerDao getOwnerDao() {
        return ownerDao;
    }

    /**
     * @param ownerDao the ownerDao to set
     */
    public void setOwnerDao(OwnerDao ownerDao) {
        this.ownerDao = ownerDao;
    }

    /**
     * @return the petDao
     */
    public PetDao getPetDao() {
        return petDao;
    }

    /**
     * @param petDao the petDao to set
     */
    public void setPetDao(PetDao petDao) {
        this.petDao = petDao;
    }

    /**
     * @return the visitDao
     */
    public VisitDao getVisitDao() {
        return visitDao;
    }

    /**
     * @param visitDao the visitDao to set
     */
    public void setVisitDao(VisitDao visitDao) {
        this.visitDao = visitDao;
    }
}


/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.dao.hibernate;

import com.spring66.training.entity.Owner;
import com.spring66.training.entity.Pet;
import com.spring66.training.entity.PetType;
import com.spring66.training.entity.Vet;
import com.spring66.training.entity.Visit;
import com.spring66.training.service.Clinic;
import java.util.Collection;
import java.util.Date;
import org.apache.commons.logging.Log;
import org.apache.commons.logging.LogFactory;
import org.springframework.test.AbstractTransactionalSpringContextTests;

/**
 *
 * @author TwinP
 */
public class ClinicHibernateTest extends AbstractTransactionalSpringContextTests{

    protected final Log log = LogFactory.getLog(getClass());
    private Clinic clinic;

    @Override
    protected String[] getConfigLocations() {
        setAutowireMode(AUTOWIRE_BY_NAME);
        return new String[]{
                    "classpath:/applicationContext.xml",
                    "classpath*:/applicationContext.xml" // for modular projects
                //"classpath:**/applicationContext*.xml" // for web projects
                };
    }

    public void testGetVets() {
        Collection<Vet> vets = this.getClinic().getVets();
        // Use the inherited countRowsInTable() convenience method (from
        // AbstractTransactionalJUnit4SpringContextTests) to verify the results.
        //assertEquals("JDBC query must show the same number of vets", super.countRowsInTable("VETS"), vets.size());
        Vet v1 = EntityUtils.getById(vets, Vet.class, 2);
        assertEquals("Leary", v1.getLastName());
        assertEquals(1, v1.getNrOfSpecialties());
        assertEquals("radiology", (v1.getSpecialties().iterator().next().getName()));
        Vet v2 = EntityUtils.getById(vets, Vet.class, 3);
        assertEquals("Douglas", v2.getLastName());
        assertEquals(2, v2.getNrOfSpecialties());
        assertEquals("dentistry", (v2.getSpecialties().iterator().next().getName()));
    //assertEquals("surgery", (v2.getSpecialties().get(1)).getName());
    }

    public void testGetPetType() {
        Collection<PetType> petTypes = this.getClinic().getPetTypes();
        PetType t1 = EntityUtils.getById(petTypes, PetType.class, 1);
        assertEquals("cat", t1.getName());
        PetType t4 = EntityUtils.getById(petTypes, PetType.class, 4);
        assertEquals("snake", t4.getName());
    }

    public void testFindOwners() {
        Collection<Owner> owners = this.clinic.findOwners("Davis");
        assertEquals(2, owners.size());
        owners = this.clinic.findOwners("Daviss");
        assertEquals(0, owners.size());
    }

    public void testLoadOwner() {
        Owner o1 = this.clinic.loadOwner(1);
        assertTrue(o1.getLastName().startsWith("Franklin"));
        Owner o10 = this.clinic.loadOwner(10);
        assertEquals("Carlos", o10.getFirstName());

        // XXX: Add programmatic support for ending transactions with the
        // TestContext Framework.

        // Check lazy loading, by ending the transaction:
        // endTransaction();

        // Now Owners are "disconnected" from the data store.
        // We might need to touch this collection if we switched to lazy loading
        // in mapping files, but this test would pick this up.
        o1.getPets();
    }

    public void testInsertOwner() {
        Collection<Owner> owners = this.clinic.findOwners("Schultz");
        int found = owners.size();
        Owner owner = new Owner();
        owner.setLastName("Schultz");
        this.clinic.storeOwner(owner);
        // assertTrue(!owner.isNew()); -- NOT TRUE FOR TOPLINK (before commit)
        owners = this.clinic.findOwners("Schultz");
        assertEquals("Verifying number of owners after inserting a new one.", found + 1, owners.size());
    }

	public void testUpdateOwner() throws Exception {
        Owner o1 = this.clinic.loadOwner(1);
        String old = o1.getLastName();
        o1.setLastName(old + "X");
        this.clinic.storeOwner(o1);
        o1 = this.clinic.loadOwner(1);
        assertEquals(old + "X", o1.getLastName());
	}

	public void testLoadPet() {
        Collection<PetType> types = this.clinic.getPetTypes();
        Pet p7 = this.clinic.loadPet(7);
        assertTrue(p7.getName().startsWith("Samantha"));
        assertEquals(EntityUtils.getById(types, PetType.class, 1).getId(), p7.getType().getId());
        assertEquals("Jean", p7.getOwner().getFirstName());
        Pet p6 = this.clinic.loadPet(6);
        assertEquals("George", p6.getName());
        assertEquals(EntityUtils.getById(types, PetType.class, 4).getId(), p6.getType().getId());
        assertEquals("Peter", p6.getOwner().getFirstName());
	}

    public void testInsertPet() {
        Owner o6 = this.clinic.loadOwner(6);
        int found = o6.getPets().size();
        Pet pet = new Pet();
        pet.setName("bowser");
        Collection<PetType> types = this.clinic.getPetTypes();
        pet.setType(EntityUtils.getById(types, PetType.class, 2));
        pet.setBirthDate(new Date());
        o6.addPet(pet);
        assertEquals(found + 1, o6.getPets().size());
        // both storePet and storeOwner are necessary to cover all ORM tools
        this.clinic.storePet(pet);
        this.clinic.storeOwner(o6);
        // assertTrue(!pet.isNew()); -- NOT TRUE FOR TOPLINK (before commit)
        o6 = this.clinic.loadOwner(6);
        //assertEquals(found + 1, o6.getPets().size());
    }


    public void testUpdatePet() throws Exception {
        System.out.println("updatePet");
        Pet p7 = this.clinic.loadPet(7);
        String old = p7.getName();
        p7.setName(old + "X");
        this.clinic.storePet(p7);
        p7 = this.clinic.loadPet(7);
        assertEquals(old + "X", p7.getName());
    }


    public void insertVisit() {
        Pet p7 = this.clinic.loadPet(7);
        int found = p7.getVisits().size();
        Visit visit = new Visit();
        p7.addVisit(visit);
        visit.setDescription("test");
        // both storeVisit and storePet are necessary to cover all ORM tools
        this.clinic.storeVisit(visit);
        this.clinic.storePet(p7);
        // assertTrue(!visit.isNew()); -- NOT TRUE FOR TOPLINK (before commit)
        p7 = this.clinic.loadPet(7);
        assertEquals(found + 1, p7.getVisits().size());
    }
    /**
     * @return the clinic
     */
    public Clinic getClinic() {
        return clinic;
    }

    /**
     * @param clinic the clinic to set
     */
    public void setClinic(Clinic clinic) {
        this.clinic = clinic;
    }
}

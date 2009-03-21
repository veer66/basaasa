/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.web.springmvc;

import com.spring66.training.entity.PetType;
import com.spring66.training.service.Clinic;
import java.beans.PropertyEditorSupport;

/**
 *
 * @author TwinP
 */
public class PetTypeEditor extends PropertyEditorSupport {

    private final Clinic clinic;

    public PetTypeEditor(Clinic clinic) {
        this.clinic = clinic;
    }

    @Override
    public void setAsText(String text) throws IllegalArgumentException {
        for (PetType type : this.clinic.getPetTypes()) {
            if (type.getName().equals(text)) {
                setValue(type);
            }
        }
    }
}

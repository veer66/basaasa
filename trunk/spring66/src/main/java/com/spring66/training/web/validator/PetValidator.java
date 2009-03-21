/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.validator;

import com.spring66.training.entity.Pet;
import org.springframework.util.StringUtils;
import org.springframework.validation.Errors;

/**
 *
 * @author TwinP
 */
public class PetValidator {

	public void validate(Pet pet, Errors errors) {
		String name = pet.getName();
		if (!StringUtils.hasLength(name)) {
			errors.rejectValue("name", "required", "required");
		}
        /*else if (pet.isNew() && pet.getOwner().getPet(name, true) != null) {
        errors.rejectValue("name", "duplicate", "already exists");
        }*/
	}

}

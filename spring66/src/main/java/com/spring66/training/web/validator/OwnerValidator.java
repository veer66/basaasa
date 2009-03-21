/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.validator;

import com.spring66.training.entity.Owner;
import org.springframework.util.StringUtils;
import org.springframework.validation.Errors;

/**
 *
 * @author TwinP
 */
public class OwnerValidator {

	public void validate(Owner owner, Errors errors) {
		if (!StringUtils.hasLength(owner.getFirstName())) {
			errors.rejectValue("firstName", "required", "required");
		}
		if (!StringUtils.hasLength(owner.getLastName())) {
			errors.rejectValue("lastName", "required", "required");
		}
		if (!StringUtils.hasLength(owner.getAddress())) {
			errors.rejectValue("address", "required", "required");
		}
		if (!StringUtils.hasLength(owner.getCity())) {
			errors.rejectValue("city", "required", "required");
		}

		String telephone = owner.getTelephone();
		if (!StringUtils.hasLength(telephone)) {
			errors.rejectValue("telephone", "required", "required");
		}
		else {
			for (int i = 0; i < telephone.length(); ++i) {
				if ((Character.isDigit(telephone.charAt(i))) == false) {
					errors.rejectValue("telephone", "nonNumeric", "non-numeric");
					break;
				}
			}
		}
	}
}

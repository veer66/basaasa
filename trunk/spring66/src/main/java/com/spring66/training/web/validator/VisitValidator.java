/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.validator;

import com.spring66.training.entity.Visit;
import org.springframework.util.StringUtils;
import org.springframework.validation.Errors;

/**
 *
 * @author TwinP
 */
public class VisitValidator {

	public void validate(Visit visit, Errors errors) {
		if (!StringUtils.hasLength(visit.getDescription())) {
			errors.rejectValue("description", "required", "required");
		}
	}

}

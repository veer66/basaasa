/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.springmvc;

import com.spring66.training.entity.Owner;
import com.spring66.training.service.Clinic;
import java.util.Collection;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;

/**
 *
 * @author TwinP
 */
@Controller
@RequestMapping("/findOwners.do")
public class FindOwnersForm {

	private final Clinic clinic;

	@Autowired
	public FindOwnersForm(Clinic clinic) {
		this.clinic = clinic;
	}

	@RequestMapping(method = RequestMethod.GET)
	public  String setupForm(Model model) {
		model.addAttribute("owner", new Owner());
		return "findOwners";
	}

	@RequestMapping(method = RequestMethod.POST)
	public  String processSubmit(Owner owner, BindingResult result, Model model) {
		// find owners by last name
		Collection<Owner> results = this.clinic.findOwners(owner.getLastName());
		if (results.size() < 1) {
			// no owners found
			result.rejectValue("lastName", "notFound", "not found");
			return "findOwners";
		}
		if (results.size() > 1) {
			// multiple owners found
			model.addAttribute("selections", results);
			return "owners";
		}
		else {
			// 1 owner found
			owner = results.iterator().next();
			return "redirect:owner.do?ownerId=" + owner.getId();
		}
	}
}

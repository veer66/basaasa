/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.springmvc;

import com.spring66.training.entity.Owner;
import com.spring66.training.entity.Pet;
import com.spring66.training.entity.PetType;
import com.spring66.training.service.Clinic;
import com.spring66.training.web.validator.PetValidator;
import java.util.Collection;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.validation.BindingResult;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestMethod;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.SessionAttributes;
import org.springframework.web.bind.support.SessionStatus;

/**
 *
 * @author TwinP
 */
@Controller
@RequestMapping("/addPet.do")
@SessionAttributes("pet")
public class AddPetForm {

	private final Clinic clinic;

	@Autowired
	public AddPetForm(Clinic clinic) {
		this.clinic = clinic;
	}

	@ModelAttribute("types")
	public Collection<PetType> populatePetTypes() {
		return this.clinic.getPetTypes();
	}

	@RequestMapping(method = RequestMethod.GET)
	public String setupForm(@RequestParam("ownerId") int ownerId, Model model) {
        Owner owner = this.clinic.loadOwner(ownerId);
        System.out.println("owner->"+owner.getFirstName());
		Pet pet = new Pet();
		//owner.addPet(pet);
        pet.setOwner(owner);
		model.addAttribute("pet", pet);
		return "petForm";
	}

	@RequestMapping(method = RequestMethod.POST)
	public String processSubmit(@ModelAttribute("pet") Pet pet, BindingResult result, SessionStatus status) {
		new PetValidator().validate(pet, result);
		if (result.hasErrors()) {
			return "petForm";
		}
		else {
            System.out.println("pet->"+pet.getOwner().getId());
			this.clinic.storePet(pet);
			status.setComplete();
			return "redirect:owner.do?ownerId=" + pet.getOwner().getId();
		}
	}
}

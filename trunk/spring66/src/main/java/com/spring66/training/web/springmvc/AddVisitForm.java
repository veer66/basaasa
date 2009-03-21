/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.springmvc;
import com.spring66.training.entity.Pet;
import com.spring66.training.entity.Visit;
import com.spring66.training.service.Clinic;
import com.spring66.training.web.validator.VisitValidator;
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
@RequestMapping("/addVisit.do")
@SessionAttributes("visit")
public class AddVisitForm {
	private final Clinic clinic;

	@Autowired
	public AddVisitForm(Clinic clinic) {
		this.clinic = clinic;
	}

	@RequestMapping(method = RequestMethod.GET)
	public String setupForm(@RequestParam("petId") int petId, Model model) {
		Pet pet = this.clinic.loadPet(petId);
		Visit visit = new Visit();
		pet.addVisit(visit);
		model.addAttribute("visit", visit);
		return "visitForm";
	}

	@RequestMapping(method = RequestMethod.POST)
	public String processSubmit(@ModelAttribute("visit") Visit visit, BindingResult result, SessionStatus status) {
		new VisitValidator().validate(visit, result);
		if (result.hasErrors()) {
			return "visitForm";
		}
		else {
			this.clinic.storeVisit(visit);
			status.setComplete();
			return "redirect:owner.do?ownerId=" + visit.getPet().getOwner().getId();
		}
	}
}

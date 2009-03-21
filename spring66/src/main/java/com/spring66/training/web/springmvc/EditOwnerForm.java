/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.web.springmvc;

import com.spring66.training.entity.Owner;
import com.spring66.training.service.Clinic;
import com.spring66.training.web.validator.OwnerValidator;
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
@RequestMapping("/editOwner.do")
@SessionAttributes("owner")
public class EditOwnerForm {

    private final Clinic clinic;

    @Autowired
    public EditOwnerForm(Clinic clinic) {
        this.clinic = clinic;
    }

    @RequestMapping(method = RequestMethod.GET)
    public String setupForm(@RequestParam("ownerId") int ownerId, Model model) {
        Owner owner = this.clinic.loadOwner(ownerId);
        model.addAttribute(owner);
        return "ownerForm";
    }

    @RequestMapping(method = RequestMethod.POST)
    public String processSubmit(@ModelAttribute Owner owner, BindingResult result, SessionStatus status) {
        System.out.println("submit");
        //return null;
        new OwnerValidator().validate(owner, result);
        if (result.hasErrors()) {
            return "ownerForm";
        } else {
            this.clinic.storeOwner(owner);
            status.setComplete();
            return "redirect:owner.do?ownerId=" + owner.getId();
        }
    }
}

/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.web.springmvc;

import com.spring66.training.entity.PetType;
import com.spring66.training.service.Clinic;
import java.util.Collection;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.AbstractController;

/**
 *
 * @author TwinP
 */
public class PetTypeListController extends AbstractController {
    private Clinic clinicService;
    @Override
    protected ModelAndView handleRequestInternal(HttpServletRequest arg0, HttpServletResponse arg1) throws Exception {
        Collection<PetType> ptList = clinicService.getPetTypes();
        ModelAndView mav = new ModelAndView("pettypeList", "pettypeList", ptList);
        mav.addObject("pettypeList", ptList);
        return mav;
    }

    /**
     * @return the clinicService
     */
    public Clinic getClinicService() {
        return clinicService;
    }

    /**
     * @param clinicService the clinicService to set
     */
    public void setClinicService(Clinic clinicService) {
        this.clinicService = clinicService;
    }

}

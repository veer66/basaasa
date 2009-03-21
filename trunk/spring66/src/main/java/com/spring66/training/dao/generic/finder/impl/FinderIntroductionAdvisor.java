package com.spring66.training.dao.generic.finder.impl;

import org.springframework.aop.support.DefaultIntroductionAdvisor;

public class FinderIntroductionAdvisor extends DefaultIntroductionAdvisor {

    public FinderIntroductionAdvisor() {
        super(new FinderIntroductionInterceptor());
    }
}

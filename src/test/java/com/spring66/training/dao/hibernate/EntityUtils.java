/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */
package com.spring66.training.dao.hibernate;

import com.spring66.training.entity.BaseEntity;
import java.util.Collection;
import org.springframework.orm.ObjectRetrievalFailureException;

/**
 *
 * @author TwinP
 */
public abstract class EntityUtils {

    /**
     * Look up the entity of the given class with the given id in the given
     * collection.
     *
     * @param entities the collection to search
     * @param entityClass the entity class to look up
     * @param entityId the entity id to look up
     * @return the found entity
     * @throws ObjectRetrievalFailureException if the entity was not found
     */
    public static <T extends BaseEntity> T getById(Collection<T> entities, Class<T> entityClass, int entityId)
            throws ObjectRetrievalFailureException {
        for (T entity : entities) {
            if (entity.getId().intValue() == entityId && entityClass.isInstance(entity)) {
                return entity;
            }
        }
        throw new ObjectRetrievalFailureException(entityClass, new Integer(entityId));
    }
}

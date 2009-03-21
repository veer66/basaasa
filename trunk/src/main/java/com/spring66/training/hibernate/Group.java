/*
 * To change this template, choose Tools | Templates
 * and open the template in the editor.
 */

package com.spring66.training.hibernate;

import java.util.Collection;
import javax.persistence.CascadeType;
import javax.persistence.Entity;
import javax.persistence.Id;
import javax.persistence.JoinColumn;
import javax.persistence.JoinTable;
import javax.persistence.ManyToMany;
import javax.persistence.OrderBy;
import javax.persistence.Table;
import javax.persistence.UniqueConstraint;
import org.hibernate.annotations.FilterDef;

/**
 *
 * @author TwinP
 */
@Entity
@Table(name = "tbl_group")
@FilterDef(name="Groupfilter")
public class Group {
	private Integer id;
    private String name;
	private Collection<Permission> permissions;

	@Id
	public Integer getId() {
		return id;
	}

	public void setId(Integer id) {
		this.id = id;
	}

	@ManyToMany(cascade = CascadeType.PERSIST)
	@JoinTable(name = "GROUPS_PERMISSIONS",
			uniqueConstraints = @UniqueConstraint(columnNames = {"group_id", "permission"}),
			joinColumns = @JoinColumn(name = "group_id", referencedColumnName = "id"),
			inverseJoinColumns = @JoinColumn(name = "permission", referencedColumnName = "permission")
	)
    @OrderBy("expirationDate")
	public Collection<Permission> getPermissions() {
		return permissions;
	}

	public void setPermissions(Collection<Permission> permissions) {
		this.permissions = permissions;
	}
}

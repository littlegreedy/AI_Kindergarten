package com.lizhou.bean;

import java.sql.Timestamp;
import java.util.List;

/**
 * 学生类
 *
 *
 */
public class Student {
	
	private int id; //ID
	
	private String number; //学号
	
	private String name; //姓名
	
	private String sex; //性别
	
	private String phone; //电话
	
	private String qq; //QQ
	
	private Clazz clazz; //班级
	
	private int clazzid; //班级ID
	
	private Grade grade; //年级
	
	private int gradeid; //年级ID

	private List<EScore> scoreList; //成绩集合

	private int one;
	private int two;
	private int three;
	private int four;
	private int five;
	private int last_week;
	private int flag;
//	private Timestamp updateTime;

//


	public int getOne() {
		return one;
	}

	public void setOne(int one) {
		this.one = one;
	}

	public int getTwo() {
		return two;
	}

	public void setTwo(int two) {
		this.two = two;
	}

	public int getThree() {
		return three;
	}

	public void setThree(int three) {
		this.three = three;
	}

	public int getFour() {
		return four;
	}

	public void setFour(int four) {
		this.four = four;
	}

	public int getFive() {
		return five;
	}

	public void setFive(int five) {
		this.five = five;
	}

	public int getLast_week() {
		return last_week;
	}

	public void setLast_week(int last_week) {
		this.last_week = last_week;
	}

	public int getFlag() {
		return flag;
	}

	public void setFlag(int flag) {
		this.flag = flag;
	}

//	public Timestamp getUpdateTime() {
//		return updateTime;
//	}




//

	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getNumber() {
		return number;
	}

	public void setNumber(String number) {
		this.number = number;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getSex() {
		return sex;
	}

	public void setSex(String sex) {
		this.sex = sex;
	}

	public String getPhone() {
		return phone;
	}

	public void setPhone(String phone) {
		this.phone = phone;
	}

	public String getQq() {
		return qq;
	}

	public void setQq(String qq) {
		this.qq = qq;
	}

	public Clazz getClazz() {
		return clazz;
	}

	public void setClazz(Clazz clazz) {
		this.clazz = clazz;
	}

	public int getClazzid() {
		return clazzid;
	}

	public void setClazzid(int clazzid) {
		Clazz clazz = new Clazz();
		clazz.setId(clazzid);
		this.clazz = clazz;
		this.clazzid = clazzid;
	}

	public Grade getGrade() {
		return grade;
	}

	public void setGrade(Grade grade) {
		this.grade = grade;
	}

	public int getGradeid() {
		return gradeid;
	}

	public void setGradeid(int gradeid) {
		Grade grade = new Grade();
		grade.setId(gradeid);
		this.grade = grade;
		this.gradeid = gradeid;
	}

}

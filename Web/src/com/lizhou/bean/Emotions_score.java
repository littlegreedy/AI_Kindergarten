package com.lizhou.bean;

import java.sql.Timestamp;

public class Emotions_score {
    private int id;

    private String number; //学号

    private int one;
    private int two;
    private int three;
    private int four;
    private int five;
    private Student student;
    private int last_week;
    private int flag;

    private Timestamp updateTime;

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public Student getStudent() {
        return student;
    }

    public void setStudent(Student student) {
        this.student = student;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

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

    public Timestamp getUpdateTime() {
        return updateTime;
    }

//    public void setUpdateTime(Timestamp updateTime) {
//        this.updateTime = updateTime;
//    }
}

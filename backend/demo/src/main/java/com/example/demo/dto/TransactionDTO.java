package com.example.demo.dto;

public class TransactionDTO {

    private Long id;
    private Double amount;
    private String type;

    public TransactionDTO() {
    }

    public TransactionDTO(Long id, Double amount, String type) {
        this.id = id;
        this.amount = amount;
        this.type = type;
    }

    public Long getId() {
        return id;
    }

    public Double getAmount() {
        return amount;
    }

    public String getType() {
        return type;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setAmount(Double amount) {
        this.amount = amount;
    }

    public void setType(String type) {
        this.type = type;
    }
}
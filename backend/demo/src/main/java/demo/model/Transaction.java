package com.example.demo.model;

import jakarta.persistence.*;
import jakarta.validation.constraints.*;

@Entity
@Table(name = "transactions")
public class Transaction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    @NotNull(message = "Amount must not be null")
    private Double amount;

    @NotBlank(message = "Type must not be blank")
    private String type;

    private Long userId;
    private boolean flagged;

    public Transaction() {
    }

    public Transaction(Long id, Double amount, String type, Long userId, boolean flagged) {
        this.id = id;
        this.amount = amount;
        this.type = type;
        this.userId = userId;
        this.flagged = flagged;
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

    public Long getUserId() {
        return userId;
    }

    public boolean isFlagged() {
        return flagged;
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

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public void setFlagged(boolean flagged) {
        this.flagged = flagged;
    }
}
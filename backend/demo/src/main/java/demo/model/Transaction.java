package com.example.demo.model;

import jakarta.persistence.*;

@Entity   // 🔥 VERY IMPORTANT
@Table(name = "transactions")
public class Transaction {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private Long userId;
    private double amount;
    private boolean flagged;

    // Getter & Setter

    public Long getId() {
        return id;
    }

    public Long getUserId() {
        return userId;
    }

    public double getAmount() {
        return amount;
    }

    public boolean isFlagged() {
        return flagged;
    }

    public void setId(Long id) {
        this.id = id;
    }

    public void setUserId(Long userId) {
        this.userId = userId;
    }

    public void setAmount(double amount) {
        this.amount = amount;
    }

    public void setFlagged(boolean flagged) {
        this.flagged = flagged;
    }
}
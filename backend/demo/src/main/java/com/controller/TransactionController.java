package com.example.demo.controller;
import com.example.demo.model.Transaction;
import com.example.demo.service.TransactionService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/transactions")
public class TransactionController {

    @Autowired
private TransactionService service;

@PostMapping
public Transaction createTransaction(@RequestBody Transaction transaction) {
    return service.processTransaction(transaction);
}

    // GET all transactions
    @GetMapping
    public List<Transaction> getAllTransactions() {
        return service.getAllTransactions();
    }
}
<<<<<<< HEAD
package com.example.demo.service;

import com.example.demo.model.Transaction;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;

public interface TransactionService {

    Page<Transaction> getAll(Pageable pageable);

    Transaction getById(Long id);

    Transaction create(Transaction transaction);
=======
package com.example.demo.service;

import com.example.demo.model.Transaction;
import com.example.demo.repository.TransactionRepository;
import com.example.demo.exception.InvalidTransactionException;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
public class TransactionService {

    @Autowired
    private TransactionRepository repository;

    // ✅ Create + Process Transaction
    public Transaction processTransaction(Transaction txn) {

        // 🔹 Validation
        if (txn.getAmount() <= 0) {
            throw new InvalidTransactionException("Amount must be greater than 0");
        }

        // 🔹 Fraud Rule (FIXED)
        if (txn.getAmount() > 10000) {
            txn.setFlagged(true);
        } else {
            txn.setFlagged(false);
        }

        // 🔹 Save to DB
        return repository.save(txn);
    }

    // ✅ Get All Transactions
    public List<Transaction> getAllTransactions() {
        return repository.findAll();
    }
>>>>>>> 8b56dea4943e3938c42ad89ae3d6eef791f34fac
}
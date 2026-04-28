<<<<<<< HEAD
package com.example.demo.service;

import com.example.demo.model.Transaction;
import java.util.List;

public interface TransactionService {

    List<Transaction> getAllTransactions();

    Transaction getTransactionById(Long id);

    Transaction createTransaction(Transaction transaction);

    Transaction updateTransaction(Long id, Transaction transaction);

    void deleteTransaction(Long id);
=======
package com.example.demo.service;

import com.example.demo.model.Transaction;
import java.util.List;

public interface TransactionService {

    List<Transaction> getAllTransactions();

    Transaction saveTransaction(Transaction t);

    void deleteTransaction(Long id);

    Transaction processTransaction(Transaction t);
>>>>>>> 804ec5a8bdcc41e93ea925ec220c88177b09285e
}
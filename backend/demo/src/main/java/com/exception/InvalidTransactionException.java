package com.example.demo.exception;

public class InvalidTransactionException extends RuntimeException {

    // Default constructor
    public InvalidTransactionException() {
        super();
    }

    // Constructor with message
    public InvalidTransactionException(String message) {
        super(message);
    }

    // Constructor with message and cause
    public InvalidTransactionException(String message, Throwable cause) {
        super(message, cause);
    }

    // Constructor with cause
    public InvalidTransactionException(Throwable cause) {
        super(cause);
    }
}
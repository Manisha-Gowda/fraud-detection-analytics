<<<<<<< HEAD
package com.example.demo.exception;

// Custom Exception for handling resource not found cases
public class ResourceNotFoundException extends RuntimeException {

    // Default Constructor
    public ResourceNotFoundException() {
        super("Resource not found");
    }

    // Constructor with custom message
    public ResourceNotFoundException(String message) {
        super(message);
    }

    // Constructor with message and cause
    public ResourceNotFoundException(String message, Throwable cause) {
        super(message, cause);
    }
=======
package com.example.demo.exception;

public class ResourceNotFoundException extends RuntimeException {
    public ResourceNotFoundException(String message) {
        super(message);
    }
>>>>>>> 804ec5a8bdcc41e93ea925ec220c88177b09285e
}
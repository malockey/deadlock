# Avoiding Deadlocks in Python

This repository contains examples of how to avoid deadlocks in Python using different algorithms and techniques.

## Algorithms Demonstrated

### 1. Wound-Wait (deadlock_wound_wait.py)

The wound-wait algorithm is an approach to avoid deadlock where older transactions "wound" (abort) newer transactions if they attempt to lock an item of data held by them. Newer transactions wait if they attempt to lock an item of data held by older transactions.

This script demonstrates the wound-wait algorithm by acquiring locks in a specific order, allowing older transactions to wound newer transactions if necessary.

### 2. Wait-Die (deadlock_wait_die.py)

The wait-die algorithm is a technique to avoid deadlock where older transactions wait if they want to lock an item of data held by a newer transaction. Newer transactions "die" if they attempt to lock an item of data held by an older transaction.

This script demonstrates the wait-die algorithm by utilizing locks with blocking acquisition. Older transactions acquire locks first, while newer transactions wait.

### 3. Timeout (deadlock_timeout.py)

The timeout algorithm is a technique to avoid deadlock where a transaction releases acquired locks if it cannot acquire a lock within a specified time limit. The transaction then retries later.

This script demonstrates the timeout algorithm by setting a timeout value when acquiring locks. If a lock cannot be acquired within the timeout period, the transaction releases the locks and retries.

### 4. Deadlock (deadlock.py)

This script demonstrates a deadlock situation in Python using threads and locks. Deadlock occurs when multiple transactions compete for the same resources and cannot proceed because each transaction is waiting for a resource held by another.

## How to Run

To execute any of the scripts, simply run the corresponding Python file. For example:

python deadlock.py
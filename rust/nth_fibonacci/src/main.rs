//! Takes in a user provided index and outputs the corresponding value from the Fibonacci Sequence.

use std::io;

/// Starting Fibonacci number.
const FIB_1: u128 = 0;
/// Second Fibonacci number.
const FIB_2: u128 = 1;

/// Entrance to the program.
fn main() {
    let n = get_user_n();

    let fib_n = get_fib_at_n_recursive(n);
    //let fib_n = get_fib_at_n(n);

    println!("Fibonacci number at index {} is {}", n, fib_n);
}

/// Gets the user input from stdin.
fn get_user_n() -> u128 {
    loop {
        println!("Enter value of index n: ");

        let mut input = String::new();

        io::stdin()
            .read_line(&mut input)
            .expect("Input is needed...");

        let input: u128 = match input.trim().parse() {
            Ok(returned_number) => {
                if returned_number == 0 {
                    println!("Index must be > 0...");
                    continue;
                } else {
                    returned_number
                }
            }
            Err(_) => {
                println!("Index must be a number...");
                continue;
            }
        };

        break input;
    }
}

/// Takes in an index and returns the Fibonacci number at that index.
fn _get_fib_at_n(n: u128) -> u128 {
    if n == 1 {
        FIB_1
    } else if n == 2 {
        FIB_2
    } else {
        let mut sequence: [u128; 3] = [FIB_1, FIB_2, FIB_1 + FIB_2];

        for _index in 4..=n {
            sequence[0] = sequence[1];
            sequence[1] = sequence[2];
            sequence[2] = sequence[0] + sequence[1];
        }

        sequence[2]
    }
}

/// A version of get_fib_at_n() that uses recursion.
fn get_fib_at_n_recursive(n: u128) -> u128 {
    match n {
        1 => FIB_1,
        2 => FIB_2,
        n => get_fib_at_n_recursive(n-2) + get_fib_at_n_recursive(n-1)
    }
}

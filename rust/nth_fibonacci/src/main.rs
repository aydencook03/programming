use std::io;

const FIB_1: u32 = 0;
const FIB_2: u32 = 1;

fn main() {
    let n = get_n();

    let fib_n = get_fib_n(n);

    println!("Fibonacci Number {} is {}", n, fib_n);
}

fn get_n() -> u32 {
    loop {
        println!("Enter value of n: ");

        let mut input = String::new();

        io::stdin()
            .read_line(&mut input)
            .expect("Input is needed...");

        let input: u32 = match input.trim().parse() {
            Ok(returned_number) => {
                if returned_number == 0 {
                    println!("Input must be > 0...");
                    continue;
                } else {
                    returned_number
                }
            }
            Err(_) => {
                println!("Input must be a number...");
                continue;
            }
        };

        break input;
    }
}

fn get_fib_n(n: u32) -> u32 {
    if n == 1 {
        FIB_1
    } else if n == 2 {
        FIB_2
    } else {
        let mut sequence: [u32; 3] = [FIB_1, FIB_2, FIB_1 + FIB_2];
        let mut index = 4;

        while index <= n {
            sequence[0] = sequence[1];
            sequence[1] = sequence[2];
            sequence[2] = sequence[0] + sequence[1];

            index += 1;
        }

        sequence[2]
    }
}
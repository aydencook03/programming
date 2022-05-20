use rand::Rng;
use std::io;

fn main() {
    println!("Guess the number!");

    let secret_number: u8 = rand::thread_rng().gen_range(1..101);

    loop {
        println!("Input your guess, from 1 to 100:");

        let mut guess = String::new();

        let _input_size = io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line.");

        let guess: u8 = match guess.trim().parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        if guess == secret_number {
            println!("You got it!");
            break;
        } else {
            if guess < secret_number {
                println!("Too low!");
            } else {
                println!("Too high!");
            }
        }
    }
}

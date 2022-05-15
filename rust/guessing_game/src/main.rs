use std::io;
use rand::Rng;

fn main() {
    println!("Guess the number!");

    let secret_number = rand::thread_rng().gen_range(1..101);

    println!("The secret number is {}", secret_number);

    println!("Input your guess:");

    let mut guess = String::new();

    let input = io::stdin();

    let size = input.read_line(&mut guess).expect("Failed to read line");

    println!("You guessed {}, this input is {} bytes", guess, size);
}
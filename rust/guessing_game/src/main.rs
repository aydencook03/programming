use std::io;

fn main() {
    println!("Guess the number!");

    println!("Input your guess:");

    let mut guess = String::new();

    let input = io::stdin();

    input.read_line(&mut guess).expect("Failed to read line");

    println!("You guessed {}", guess);
}

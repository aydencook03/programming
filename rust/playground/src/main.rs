fn main() {
    let index = 45;
    let value = fib(index);
    println!("{}", value);
}

fn fib(index: usize) -> usize {
    match index {
        0 => {
            println!("Must be over 0");
            0
        }
        1 => 0,
        2 => 1,
        _ => fib(index - 1) + fib(index - 2),
    }
}

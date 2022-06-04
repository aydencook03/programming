

fn main() {
    let index = 45;
    let value = fib_match(index);
    println!("{}", value);
}

fn fib(index: usize) -> usize {
    if index == 0 {
        return 0;
    } else if index == 1 {
        return 0;
    } else if index == 2 {
        return 1;
    } else {
        return fib(index - 1) + fib(index - 2);
    }
}

fn fib_match(index: usize) -> usize {
    match index {
        0 => 0,
        1 => 0,
        2 => 1,
        _ => fib_match(index - 1) + fib_match(index - 2),
    }
}

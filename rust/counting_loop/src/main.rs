fn main() {
    println!("Starting...");

    let mut counter = 0;

    let value = loop {
        if counter < 100 {
            counter += 1;
            println!("{}", counter);
        } else {
            break "Done!";
        }
    };

    println!("{}", value);
}
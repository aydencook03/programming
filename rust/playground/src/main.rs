fn main() {
    let val: Option<String> = Some(String::from("Hello"));

    let integer = val.as_ref().unwrap();
    println!("{:#?}", integer);
    println!("{:#?}", val);
}

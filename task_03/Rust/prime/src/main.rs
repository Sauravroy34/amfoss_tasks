use std::io;
fn main () {
    let mut number = String::new();
    println!("enter number");
    io::stdin().read_line(&mut number).expect("failed to input");
    let number:u32 = number.trim().parse().expect("failed to convert");
    if number <2 {
        println!("sorry prime number not defined for this range");
    }
    for i in 2..number+1 {
        if check(i){
            println!("prime number :{}",i)
        }

    }

}

fn check(num:u32) -> bool {
    if num == 2{
        return true;
    }
    else{
        for i in 2..num{
            if num%i == 0 {
                return false;
            }
        }
    }
    return true;
}
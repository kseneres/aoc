use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let input = get_input(); 

    part_one(&input); 
    part_two(&input); 
}

// Find two entries that sum to 2020 and multiply the two numbers. 
fn part_one(input: &Vec<i32>) {
    for i in 0..input.len() {
        for j in i..input.len() {
            let a = input[i];
            let b = input[j];

            if (a + b) == 2020 {
                println!("{} * {} = {}", a, b, a*b); 
            }
        }
    }
}

// Find three entries that sum to 2020 and multiply the numbers. 
fn part_two(input: &Vec<i32>) {
    for i in 0..input.len() {
        for j in i..input.len() {
            for k in j..input.len() {
                let a = input[i];
                let b = input[j];
                let c = input[k];

                if (a + b + c) == 2020 {
                    println!("{} * {} * {} = {}", a, b, c, a*b*c); 
                }
            }
        }
    }
}

fn get_input() -> Vec<i32> {
    let mut input: Vec<i32>= vec![];

    // TODO: catch errors (stop unwrapping)
    let filename = "input";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file); 
    
    for line in reader.lines() {
        let line = line.unwrap(); 
        input.push(line.parse().unwrap()); 
    }

    input 
}

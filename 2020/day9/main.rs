use std::fs::File;
use std::io::{BufRead, BufReader};

const WINDOW: usize = 25;

fn main() {
    let input = get_input(); 

    let mut numbers: Vec<u64> = vec![]; 
    for line in input {
        numbers.push(line.parse().unwrap()); 
    }

    for i in 0..numbers.len()-1 {
        let window = &numbers[i..i+WINDOW]; 
        let target: u64 = numbers[i + WINDOW];

        let found = find_target(window, target); 

        if !found {
            println!("weak: {}", target); 
            break;
        }
    }
}

fn find_target(numbers: &[u64], target: u64) -> bool {
    let mut found = false; 
    for i in 0..numbers.len() {
        for j in i+1..numbers.len() {
            if numbers[i] + numbers[j] == target {
                found = true; 
                break;
            }
        }

        if found {
            break;
        }
    }

    found
}

fn get_input() -> Vec<String> {
    let mut input: Vec<String>= vec![];

    // TODO: catch errors (stop unwrapping)
    let filename = "input";
    let file = File::open(filename).unwrap();
    let reader = BufReader::new(file); 
    
    for line in reader.lines() {
        let line = line.unwrap(); 
        input.push(line); 
    }

    input 
}

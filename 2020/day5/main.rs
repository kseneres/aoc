use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let input = get_input(); 

    let mut ids: Vec<u32> = vec![]; 
    for line in input {
        let id = get_seat_id(&line); 
        ids.push(id); 
    }

    ids.sort(); 

    let max_id = ids.iter().max().unwrap(); 
    println!("highest id: {}", max_id); 

    let mut seat_id = 0; 
    for i in 1..ids.len() {
        if ids[i] - ids[i - 1] == 2 {
            seat_id = ids[i] - 1; 
        }
    }

    println!("seat id: {}", seat_id); 
}

fn get_seat_id(boarding_pass: &String) -> u32 {
    let mut row: u8 = 0b0111_1111;
    let mut col: u8 = 0b0000_0111;
    
    let mut mask: u8 = 0b0100_0000; 
    for c in boarding_pass.chars().take(7) {
        if c == 'F' {
            row &= !mask; 
        }
        mask >>=1; 
    }

    mask = 0b0000_0100; 
    for c in boarding_pass.chars().skip(7).take(3) {
        if c == 'L' {
            col &= !mask; 
        }
        mask >>=1; 
    }

    u32::from(row) * 8 + u32::from(col)
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

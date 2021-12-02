use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let input = get_input(); 
    
    let mut answer = String::new(); 
    let mut part_one_count = 0; 

    for (i, line) in input.iter().enumerate() {
        answer.push_str(&line); 

        if line.trim().is_empty() || i == input.len() - 1 {
            let mut all_answers: Vec<char> = answer.chars().collect();
            all_answers.sort();
            all_answers.dedup(); 

            part_one_count += all_answers.len(); 
            answer.clear(); 
        }
    }
    println!("part one count: {}", part_one_count); 

    let mut answers: Vec<char> = Vec::new(); 
    let mut part_two_count = 0; 
    let mut reset = true; 

    for (i, line) in input.iter().enumerate() {
        if line.trim().is_empty() || i == input.len() - 1 {
            part_two_count += answers.len(); 
            answers.clear(); 
            reset = true; 
        }

        let chars: Vec<char> = line.chars().collect();
        if !chars.is_empty() {
            if reset {
                answers.extend_from_slice(&chars); 
                reset = false; 
            } else {
                answers.retain(|c| chars.contains(c)); 
            }
        }
    }

    println!("part two count: {}", part_two_count); 
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

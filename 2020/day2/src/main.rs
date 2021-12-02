use std::fs::File;
use std::io::{BufRead, BufReader};

use regex::Regex;

fn main() {
    let input = get_input(); 

    let re = Regex::new(r"^(\d+)-(\d+) (\w): (\w+)$").unwrap();  
    let mut valid_count_part_1 = 0; 
    let mut valid_count_part_2 = 0; 

    for line in input {
        let caps = re.captures(&line).unwrap(); 
        let num_1: usize = caps.at(1).unwrap().parse().unwrap(); 
        let num_2: usize = caps.at(2).unwrap().parse().unwrap(); 
        let letter = caps.at(3).unwrap().chars().nth(0).unwrap(); 
        let pw = caps.at(4).unwrap(); 

        if part_one_match(num_1, num_2, letter, pw) {
            valid_count_part_1 += 1;
        }

        if part_two_match(num_1, num_2, letter, pw) {
            valid_count_part_2 += 1; 
        }
    }

    println!("part 1 valid count: {}", valid_count_part_1); 
    println!("part 2 valid count: {}", valid_count_part_2); 
}

fn part_two_match(position_1: usize, position_2: usize, letter: char, pw: &str) -> bool {
    let mut char_indices = pw.chars(); 

    let letter_1 = char_indices.nth(position_1 - 1).unwrap(); 
    let letter_2 = char_indices.nth(position_2 - position_1 - 1).unwrap(); 

    println!("{} - {}, {}-{}, {}-{}", pw, letter, position_1, position_2, letter_1, letter_2); 

    (letter_1 == letter || letter_2 == letter) && letter_1 != letter_2
}

fn part_one_match(min: usize, max: usize, letter: char, word: &str) -> bool {
    let v: Vec<&str> = word.matches(letter).collect(); 
    let match_count = v.len();

    match_count >= min && match_count <= max 
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

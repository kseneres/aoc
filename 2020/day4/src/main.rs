#[macro_use]
extern crate lazy_static; 

use std::fs::File;
use std::io::{BufRead, BufReader};

use regex::Regex;

fn main() {
    let input = get_input(); 
    
    let mut passports: Vec<String> = vec![]; 
    let mut passport = String::new(); 

    for line in input {
        if line.trim().is_empty() {
            passports.push(passport);  
            passport = String::new(); 
        } else {
            passport.push_str(&line); 
            passport.push_str(" "); 
        }
    }
    passports.push(passport); 

    lazy_static! {
        static ref BYR_RE: Regex = Regex::new(r".*byr:(\d{4})").unwrap(); 
        static ref IYR_RE: Regex = Regex::new(r".*iyr:(\d{4})").unwrap(); 
        static ref EYR_RE: Regex = Regex::new(r".*eyr:(\d{4})").unwrap(); 
        static ref HGT_RE: Regex = Regex::new(r".*hgt:(\d{2,3})(cm|in)").unwrap(); 
        static ref HCL_RE: Regex = Regex::new(r".*hcl:#[\da-f]{6}").unwrap(); 
        static ref ECL_RE: Regex = Regex::new(r".*ecl:(amb|blu|brn|gry|grn|hzl|oth){1}").unwrap(); 
        static ref PID_RE: Regex = Regex::new(r".*pid:(\d{9}) .*").unwrap(); 
    }

    let mut valid_count = 0; 
    for passport in passports {
        let byr = validate_year(&BYR_RE, &passport, 1920, 2002); 
        let iyr = validate_year(&IYR_RE, &passport, 2010, 2020); 
        let eyr = validate_year(&EYR_RE, &passport, 2020, 2030); 
        let hgt = validate_height(&HGT_RE, &passport); 

        let hcl = HCL_RE.is_match(&passport); 
        let ecl = ECL_RE.is_match(&passport); 

        let pid = validate_pid(&PID_RE, &passport); 

        if byr && iyr && eyr && hgt && hcl && ecl && pid {
            valid_count += 1; 
        }
    }

    println!("valid passports: {}", valid_count); 
}

fn validate_year(re: &Regex, passport: &String, start: usize, end: usize) -> bool {
    let year = get_value(re, passport).parse().unwrap_or(0); 

    year >= start && year <= end
}

fn validate_height(re: &Regex, passport: &String) -> bool {
    if re.is_match(passport) {
        let captures = re.captures(passport).unwrap(); 
        let value = captures.at(1).unwrap().parse().unwrap_or(0); 
        let unit = captures.at(2).unwrap(); 

        if unit == "cm" {
            value >= 150 && value <= 193
        } else if unit == "in" {
            value >= 59 && value <= 76
        } else {
            false
        }
    } else {
        false
    }
}

fn validate_pid(re: &Regex, passport: &String) -> bool {
    let id = get_value(re, passport).parse::<usize>();

    id.is_ok()
}

fn get_value(re: &Regex, line: &String) -> String {
    if re.is_match(line) {
        re.captures(line).unwrap()
            .at(1)
            .map(|s| s.to_string())
            .unwrap_or(String::new()) 
    } else {
        String::new()
    }
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

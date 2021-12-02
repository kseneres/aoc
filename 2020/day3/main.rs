use std::fs::File;
use std::io::{BufRead, BufReader};
use std::fmt;

struct Traversal {
    right: usize,
    down: usize,
    right_position: usize,
    count: usize
}

const TREE: char = '#';

impl Traversal {
    fn new(right: usize, down: usize) -> Self {
        Self {
            right, 
            down, 
            right_position: 0,
            count: 0
        }
    }

    fn check(&mut self, line: &str, down_position: usize) {
        if down_position % self.down != 0 {
            return; 
        }

        self.right_position += self.right; 

        let index = self.right_position % line.len(); 
        let location = line.chars().nth(index).unwrap(); 

        if location == TREE {
            self.count += 1; 
        }
    }
}

impl fmt::Display for Traversal {
    fn fmt(&self, f: &mut fmt::Formatter) -> fmt::Result {
        write!(f, "right: {}, down: {}, tree count: {}", self.right, self.down, self.count)
    }
}

fn main() {
    let input = get_input(); 

    let mut t1 = Traversal::new(1, 1);
    let mut t2 = Traversal::new(3, 1);
    let mut t3 = Traversal::new(5, 1);
    let mut t4 = Traversal::new(7, 1);
    let mut t5 = Traversal::new(1, 2);

    for i in 1..input.len() {
        let line = &input[i]; 

        t1.check(line, i); 
        t2.check(line, i); 
        t3.check(line, i); 
        t4.check(line, i); 
        t5.check(line, i); 
    }

    println!("{}", t1.to_string()); 
    println!("{}", t2.to_string()); 
    println!("{}", t3.to_string()); 
    println!("{}", t4.to_string()); 
    println!("{}", t5.to_string()); 

    let answer = t1.count * t2.count * t3.count * t4.count * t5.count; 
    println!("answer: {}", answer); 
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

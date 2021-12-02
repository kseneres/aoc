use std::fs::File;
use std::io::{BufRead, BufReader};

#[derive(PartialEq)]
enum Operation {
    NOP,
    ACC,
    JMP
}

impl Operation {
    fn to_str(&self) -> &str {
        match self {
            Operation::NOP  => "nop",
            Operation::ACC  => "acc",
            Operation::JMP  => "jmp",
        }
    }

    fn from_str(input: &str) -> Operation {
        match input {
            "nop"   => Operation::NOP,
            "acc"   => Operation::ACC,
            "jmp"   => Operation::JMP,
            _       => Operation::NOP
        }
    }
}

struct Instruction {
    operation: Operation, 
    arg: i32
}

fn main() {
    let input = get_input(); 

    let mut instructions: Vec<Instruction> = Vec::new(); 
    for line in input {
        let parts: Vec<&str>= line.split(' ').collect(); 
        
        let op = Operation::from_str(parts[0]);
        let arg = parts[1].parse().unwrap_or(-1); 

        instructions.push(Instruction {
            operation: op,
            arg: arg
        }); 
    }

    let mut acc = 0; 
    let mut pc: usize = 0; 
    let mut executed_instructions: Vec<usize> = vec![]; 

    loop {
        let i = &instructions[pc]; 
        let pc_change = match i.operation {
            Operation::NOP  => 1,
            Operation::ACC  => 1,
            Operation::JMP  => i.arg,
        };

        let new_pc: usize = (pc as i32 + pc_change) as usize; 
        if executed_instructions.contains(&new_pc) {
            break;
        } else {
            executed_instructions.push(pc); 
            pc = new_pc; 
        }

        if i.operation == Operation::ACC {
            acc += i.arg; 
        }
    }

    println!("acc: {}", acc); 

    let mut changed_instruction_index = 0; 
    let mut success = false; 

    let attempts: Vec<usize> = instructions.iter()
        .enumerate()
        .filter_map(|(i, e)| if e.operation == Operation::NOP || e.operation == Operation::JMP { Some(i) } else { None })
        .collect(); 

    let mut attempt_iter = attempts.iter(); 
    
    let mut try = false; 
    while !success {

        changed_instruction_index = *attempt_iter.next().unwrap_or(&0); 

        pc = 0; 
        acc = 0; 
        executed_instructions.clear(); 
        println!("loop"); 

        loop {
            let i = &instructions[pc]; 
            let operation = if pc == changed_instruction_index {
                if i.operation == Operation::NOP {
                    &Operation::JMP
                } else {
                    &Operation::NOP
                }
            } else {
                &i.operation
            };

            println!("{} {}", operation.to_str(), i.arg); 

            let pc_change = match operation {
                Operation::NOP  => 1,
                Operation::ACC  => 1,
                Operation::JMP  => i.arg,
            };
            let new_pc: usize = (pc as i32 + pc_change) as usize; 

            if i.operation == Operation::ACC {
                acc += i.arg; 
            }
            if success {
                break
            }

            if new_pc == instructions.len() - 1 {
                success = true;
            }


            if executed_instructions.contains(&new_pc) {
                break;
            } else {
                executed_instructions.push(pc); 
                pc = new_pc; 
            }


        }

        changed_instruction_index += 1;
    }

    println!("acc: {}", acc); 
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

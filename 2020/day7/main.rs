use std::fs::File;
use std::io::{BufRead, BufReader};

struct Bag {
    color: String,
    count: u32
}

struct Rule {
    outer_bag_color: String,
    inner_bags: Vec<Bag>
}

fn main() {
    let input = get_input(); 
    let mut rules: Vec<Rule> = Vec::new(); 

    for line in input {
        let rule: Vec<&str> = line.split("bag").collect(); 

        let outer_bag_color = rule[0].trim().to_string(); 
        let mut inner_bags: Vec<Bag> = Vec::new(); 

        // skip last item, which just contains period
        for i in 1..rule.len()-1 {
            let pos = rule[i].find(char::is_numeric); 

            if let Some(x) = pos {
                let bag_count = rule[i].chars().nth(x).unwrap_or('0').to_digit(10).unwrap_or(0); 
                let bag_color = rule[i].chars().skip(x+1).collect::<String>().trim().to_string(); 

                inner_bags.push(Bag {
                    color: bag_color,
                    count: bag_count
                }); 
            }
        }

        rules.push(Rule {
            outer_bag_color: outer_bag_color, 
            inner_bags: inner_bags 
        });
    }

    let start_bag = "shiny gold"; 
    let mut target_bags: Vec<String> = [start_bag.to_string()].to_vec(); 
    let mut container_bags: Vec<String> = vec![]; 
    let mut count = 0; 

    while !target_bags.is_empty() {
        for rule in &rules {
            if rule.inner_bags.iter().any(|bag| target_bags.contains(&bag.color)) {
                container_bags.push(rule.outer_bag_color.clone());  
            }
        }

        count += container_bags.len(); 
        rules.retain(|r| !container_bags.contains(&r.outer_bag_color)); 

        target_bags.clear();
        target_bags.append(&mut container_bags); 
    }

    println!("count: {}", count); 


    let start_rule = rules.iter().find(|r| r.outer_bag_color == start_bag).unwrap(); 
    let nested_bag_count = get_nested_bag_count(&rules, &start_rule); 

    println!("nested bag count: {}", nested_bag_count); 
}

fn get_nested_bag_count(rules: &Vec<Rule>, rule: &Rule) -> u32 {
    if rule.inner_bags.is_empty() {
        0
    } else {
        let mut total = 0; 
        for bag in &rule.inner_bags {
            let nested_rule = rules.iter().find(|r| r.outer_bag_color == bag.color).unwrap(); 
            let nested_count = bag.count + bag.count * get_nested_bag_count(rules, nested_rule); 
            total += nested_count; 
        }

        total
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

use regex::Regex;
use std::fs;

fn read_data() -> Vec<String> {
    const FILE_PATH: &str = "data/input.txt";

    let data: Vec<String> = fs::read_to_string(FILE_PATH)
        .unwrap()
        .lines()
        .map(String::from)
        .collect();

    return data;
}

// part 1, count number of times the rotations stop at exactly zero
fn count_dial_at_zero(data: &Vec<String>) -> () {
    let mut dial: i16 = 50;
    let mut count: i16 = 0;
    let re = Regex::new(r"(L|R)(\d+)").unwrap();

    // parse each line as an individual string
    for d in data {
        // use regex to split each line into two groups; (L or R) and (number)
        let caps = re.captures(&d).unwrap();
        let dir = caps.get(1).unwrap().as_str();
        let num: i16 = caps
            .get(2)
            .unwrap()
            .as_str()
            .parse::<i16>()
            .expect("Err parsing str to i16");

        // subtract or add to dial depending on rotation direction
        if dir == "L" {
            for _i in 0..num {
                dial -= 1;

                // if dial reaches 0, set it back to 99
                if dial < 0 {
                    dial = 99;
                }
            }
        // right rotation increases dial number
        } else if dir == "R" {
            for _i in 0..num {
                dial += 1;

                // if dial reaches 100, set it back 0
                if dial > 99 {
                    dial = 0;
                }
            }
        }

        // count total number of times dial points at 0
        if dial == 0 {
            count += 1;
        }
    }
    println!("The dial rotated to zero {count} times");
}

// p2, count times dial reach 0 during any rotation
fn count_clicks_at_zero(data: &Vec<String>) -> () {
    let mut dial: i16 = 50;
    let mut clicks: i16 = 0;
    let re = Regex::new(r"(L|R)(\d+)").unwrap();

    // parse each line as an individual string
    for d in data {
        // use regex to split each line into two groups; (L or R) and (number)
        let caps = re.captures(&d).unwrap();
        let dir = caps.get(1).unwrap().as_str();
        let num: i16 = caps
            .get(2)
            .unwrap()
            .as_str()
            .parse::<i16>()
            .expect("Err parsing str to i16");

        // subtract or add to dial depending on rotation direction
        if dir == "L" {
            for _i in 0..num {
                dial -= 1;

                // set it back to 99, and check dial position
                if dial < 0 {
                    dial = 99;
                }
                if dial == 0 {
                    clicks += 1;
                }
            }
        // right rotation increases dial number
        } else if dir == "R" {
            for _i in 0..num {
                dial += 1;

                // set it back 0, and check dial position
                if dial > 99 {
                    dial = 0;
                }
                if dial == 0 {
                    clicks += 1;
                }
            }
        }
        // println!("{}, {}, {}", d, dial, clicks);
    }
    println!("The dial clicked at zero {clicks} times");
}

fn main() {
    let data: Vec<String> = read_data();
    count_dial_at_zero(&data);
    count_clicks_at_zero(&data);
}

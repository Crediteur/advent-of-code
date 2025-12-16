use std::fs;

// read input string and split by "," delimiter and collect into vector
fn read_data() -> Vec<String> {
    const FILE_PATH: &str = "input.txt"; //location to txt file

    let data: Vec<String> = fs::read_to_string(FILE_PATH)
        .expect("Err reading file")
        .split(',')
        .map(String::from)
        .collect();

    return data;
}

// further seperate string elements by "-" delimiter and convert into int tuple pairs
fn parse_data(data: &Vec<String>) -> Vec<(i64, i64)> {
    let mut data_tup: Vec<(i64, i64)> = Vec::new(); // initialize empty vector

    for d in data {
        let pairs: Vec<i64> = d.split("-").map(|p| p.parse::<i64>().unwrap()).collect();
        data_tup.push((pairs[0], pairs[1]));
    }

    return data_tup;
}

// counts the length of an integer number
fn n_length(n: i64) -> i64 {
    let num: u32 = n.checked_ilog10().unwrap_or(0) + 1;
    let num: i64 = num.try_into().unwrap();
    return num;
}

// turns a vector into an iter and compares all elements to the first
// returns true if all elements are exactly the same
fn is_all_same<T>(vec: &[T]) -> bool
where
    T: PartialEq,
{
    let mut iter = vec.iter();
    let first = iter.next();

    iter.fold(first, |acc, item| {
        acc.and_then(|stored| if stored == item { Some(stored) } else { None })
    })
    .is_some()
}

// part 1, find and sum palindrome IDs
// assumption: only even length numbers can be palindromes
//   eg. sum 341341 bc (341 == 341)
fn sum_invalid_id(data: &Vec<(i64, i64)>) -> i64 {
    let mut sum: i64 = 0;

    // iterate through each pair of IDs
    for pair in data {
        let start = pair.0;
        let last = pair.1;

        // check all values between start and last ID
        for id in start..=last {
            let id_len = n_length(id);

            // check if num length is even (minor optimization)
            if id_len % 2 == 0 {
                let id_str = id.to_string();
                let (first_half, second_half) = id_str.split_at(id_str.len() / 2); // split the number in half and compare
                if first_half == second_half {
                    sum += id
                }
            }
        }
    }

    return sum;
}

// part 2, find all numbers that represent repeated substrings
// by finding the repeating substring chunks in the id string
fn more_invalid_id(data: &Vec<(i64, i64)>) -> i64 {
    let mut sum: i64 = 0;

    // iterate through each pair of IDs
    for pair in data {
        let start = pair.0;
        let last = pair.1;

        // check all values between start and last ID
        for id in start..=last {
            let id_len: i64 = n_length(id);
            let mut len_gcd: Vec<i64> = Vec::new();
            let id_str = id.to_string();

            // find all gcds of id_len, such that they are perfectly divisble
            for i in 2i64..=id_len {
                if id_len % i == 0 {
                    len_gcd.push(i);
                }
            }

            // split string id into chunks based on len_gcd values
            // and check if all chunks are equivalent
            for num in len_gcd {
                let chunk: usize = (id_len / num).try_into().unwrap(); // size of each chunk based on len gcd
                let chars: Vec<char> = id_str.chars().collect(); // split id_str into chars
                let split = &chars // collect chars into a vector based on chunk size
                    .chunks(chunk)
                    .map(|chunk| chunk.iter().collect::<String>())
                    .collect::<Vec<String>>();

                // if all elements are exactly the same substring
                // it is an invalid id, so add it to sum and break
                if is_all_same(split) {
                    sum += id;
                    break;
                }
            }
        }
    }

    return sum;
}

fn main() {
    let data: &Vec<String> = &read_data();
    let data: &Vec<(i64, i64)> = &parse_data(data);
    println!("The sum of invalid IDs is {}", sum_invalid_id(&data));
    println!("The sum of more invalid IDs is {}", more_invalid_id(&data));
}

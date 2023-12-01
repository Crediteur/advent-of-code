// Lowercase item types a through z have priorities 1 through 26.
// Uppercase item types A through Z have priorities 27 through 52.

const fs = require("fs");

fs.readFile("input.txt", "utf8", (err, data) => {
  let splitData = data.trim().split("\r\n");

  // oddEven(splitData);
  scoreMatch(splitData);
  scoreTeam(splitData);
});

const scoreTeam = (data) => {
  let sum = 0;
  for (let i = 3; i < data.length + 1; i += 3) {
    let dict = {};
    let elf1 = data[i - 3];
    let elf2 = data[i - 2];
    let elf3 = data[i - 1];

    // too lazy to do optimal n solution, so do a triple loop
    match: for (const letter1 of elf1) {
      for (const letter2 of elf2) {
        for (const letter3 of elf3) {
          if (letter1 === letter2 && letter2 === letter3) {
            // match found, check if letter is uppercase or lower and add to sum
            let match = letter1;
            if (match == match.toUpperCase()) sum += letter1.charCodeAt(0) - 38;
            else sum += letter1.charCodeAt(0) - 96;

            break match;
          }
        }
      }
    }
  }
  console.log(sum);
};

const scoreMatch = (data) => {
  let sum = 0;
  for (const str of data) {
    // split each string into left and right substrings
    const middle = str.length / 2;
    const left = str.substr(0, middle);
    const right = str.substr(middle, str.length);

    // find matching letter in both susbtrings
    match: for (const letterL of left) {
      for (const letterR of right) {
        if (letterL === letterR) {
          // match found, check if letter is uppercase or lower and add to sum
          let match = letterL;
          if (match == match.toUpperCase()) sum += letterL.charCodeAt(0) - 38;
          else sum += letterL.charCodeAt(0) - 96;

          break match;
        }
      }
    }
  }
  console.log(`part one: ${sum}`);
};

// check if items are odd or even length
// findings: no odd length items in sacks
// const oddEven = (data) => {
//   let odd = 0;
//   let even = 0;
//   for (const sack of data) {
//     if (sack.length % 2 == 0) {
//       even++;
//     } else {
//       odd++;
//     }
//   }
//   console.log(odd, even);
// };

// console.log("Z".charCodeAt(0));

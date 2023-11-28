//import {readFile} from "fs";
const fs = require("fs");

// input file is read as a huge string
fs.readFile("input.txt", "utf8", (err, data) => {
  let splitData = data.split("\r\n");

  biggestElf(splitData);
  topThree(splitData);
});

const topThree = (data) => {
  let calories = [];
  let sum = 0;
  for (const c of data) {
    // sum each line while it is not a an empty space
    if (c !== "") sum += Number(c);
    // empty space, push each value to the array
    else {
      calories.push(sum);
      sum = 0;
    }
  }
  // proper sorting method of JavaScript, decreasing
  calories.sort((a, b) => b - a);
  const top3 = calories[0] + calories[1] + calories[2];
  console.log(`top 3 elves: ${top3}`);
};

const biggestElf = (data) => {
  let maxCalorie = 0;
  let sum = 0;
  for (const c of data) {
    // sum each line while it is not a an empty space
    if (c !== "") {
      sum += Number(c);
    }
    // empty space, check max sum
    else {
      if (sum > maxCalorie) {
        maxCalorie = sum;
      }
      sum = 0;
    }
  }
  console.log(`elf with the most calories: ${maxCalorie}`);
};

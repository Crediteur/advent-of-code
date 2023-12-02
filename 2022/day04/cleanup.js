const fs = require("fs");

const main = () => {
  fs.readFile("input.txt", "utf8", (err, data) => {
    let splitData = data.trim().split("\r\n");

    containingPairs(splitData);
    overlappingPairs(splitData);
  });
};

// part two
const overlappingPairs = (data) => {
  let sum = 0;

  for (let line of data) {
    let overlap = false;
    [elf1, elf2] = cleanData(line);

    // check elf1 overlap in elf2
    if (
      (elf1[0] >= elf2[0] && elf1[0] <= elf2[1]) ||
      (elf1[1] >= elf2[0] && elf1[1] <= elf2[1])
    ) {
      overlap = true;
    }

    // check elf2 overlap in elf1
    if (
      !overlap &&
      ((elf2[0] >= elf1[0] && elf2[0] <= elf1[1]) ||
        (elf2[1] >= elf1[0] && elf2[1] <= elf1[1]))
    ) {
      overlap = true;
    }

    if (overlap) sum += 1;
  }

  // i cant believe this was the right answer
  console.log(`overlapping pairs: ${sum}`);
};

// part one
const containingPairs = (data) => {
  let sum = 0;

  for (let line of data) {
    let contained = false;
    [elf1, elf2] = cleanData(line);

    // check elf1 contained in elf2
    if (elf1[0] >= elf2[0] && elf1[1] <= elf2[1]) {
      contained = true;
    }

    // check elf2 contained in elf1
    if (!contained && elf2[0] >= elf1[0] && elf2[1] <= elf1[1]) {
      contained = true;
    }
    if (contained) sum += 1;
  }

  console.log(`containing pairs: ${sum}`);
};

// clean each string line and return numbers
const cleanData = (line) => {
  let ranges = line.split("-").join(",").split(",");
  // elf1min, elf1max, elf2min. elf2max
  return [
    [Number(ranges[0]), Number(ranges[1])],
    [Number(ranges[2]), Number(ranges[3])],
  ];
};

main();

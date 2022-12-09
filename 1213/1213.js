const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let englishName = input[0];
  let checkImpossible = 0;
  let oddChar = "";
  const result = [];

  const alphaArr = new Array(26).fill(0);
  for (let i = 0; i < englishName.length; i++) {
    alphaArr[englishName[i].charCodeAt(0) - 65] += 1;
  }
  alphaArr.forEach((e, idx) => {
    if (e % 2 === 1) {
      checkImpossible += 1;
      oddChar += String.fromCharCode(idx + 65);
    }
    if (e !== 0) {
      for (let i = 0; i < parseInt(alphaArr[idx] / 2); i++) {
        result.push(String.fromCharCode(idx + 65));
      }
    }
  });
  if (checkImpossible > 1) return console.log("I'm Sorry Hansoo");
  result.push(oddChar);
  for (let i = result.length - 2; i >= 0; i--) {
    result.push(result[i]);
  }
  return console.log(result.join(""));
}

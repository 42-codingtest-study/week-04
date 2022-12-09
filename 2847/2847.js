const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  const n = input[0] * 1;
  const arr = [];
  let answer = 0;
  for (let i = 1; i <= n; i++) {
    arr.push(input[i] * 1);
  }
  for (let i = n; i > 0; i--) {
    let temp = arr[i - 1];
    while (arr[i - 2] >= temp) {
      arr[i - 2]--;
      answer++;
    }
  }
  console.log(answer);
}
// 입국심사 BOJ 3079 송근일 gsong 24살 991206 (곧 생일)
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().split("\n");
// 표준 입력으로 받아도 되고 mac 환경에선 input.txt로 받을 수 도 있게 해주는 코드
solution(input);

function solution(input) {
  let simsa = BigInt(input[0].split(" ")[0]);
  let num = BigInt(input[0].split(" ")[1]);
  const simsaArr = [];
  for (let i = 0; i < simsa; i++) {
    simsaArr.push(BigInt(input[i + 1]));
  }
  // 입력값 받기 (입력값의 범위가 크기 때문에BigInt를 사용한다.)
  let left, right, mid, result;
  left = 0n;
  right = 10n ** 9n * num;
  //  left, right 값 설정을 0과 범위 최댓값으로 지정했다.
  result = right;
  while (left < right) {
    mid = BigInt((left + right) / 2n);

    let answer = 0n;
    simsaArr.forEach((e) => {
      answer += BigInt(mid / BigInt(e));
    });
    // mid일때의 몫 계산을 해준다.
    if (answer < num) {
      left = mid + 1n;
    } else {
      right = mid;
    }
  }
  console.log(right.toString());
}
//풀었다 야호~

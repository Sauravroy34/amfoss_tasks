function isPrime(num) {
  if (num ==2) {
    return true;
  }

  for (let i = 2; i<num; i++) {
    if (num % i === 0) {
      return false;
    }
  }

  return true;
}
const n = prompt("Enter a number: ");
if (n<2) {
  console.log("prime number not defined for this range")
}
for (let i =2;i<=n;i++) {
  if (isPrime(i)){
    console.log(`the prime number :${i}`)
  }
}



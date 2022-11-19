const myAtoi = (s) => {
  // Implement the myAtoi(string s) function
  // -> converts a string to a 32-bit signed integer
  // (similar to C/C++'s atoi function).

  let i = 0;
  let sign = 1;
  while (s[i] === ' ') {
    console.log(`at ${i} and expected whitespace`);
    i++;
  }
  
  if (s[i] === '+') {
    i++;
  } else if (s[i] === '-') {
    sign = -1;
    i++;
  }
  
  const start = i;

  while (s[i] >= '0' && s[i] <= '9') {
    i++;
  }

  let result =  sign * Number(s.slice(start, i));

  result = result > 2**31 -1 ? 2**31 - 1 : result;
  result = result < -1 * 2**31 ? -1 * 2**31 : result;

  return result;
};

// console.log(myAtoi('      fart '));
console.log(myAtoi('123"   '));


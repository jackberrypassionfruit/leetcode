const longestPalindrome = (s) => {
    
  const isPalindrome = (s) => {
      let isPal = true;
      for (let i = 0; i< (str.length - 1 ) / 2; i++) {
          if (str[i] != str[str.length - i - 1]) {
              isPal = false;
          }
      }
      return isPal;
  }
  
  const expandChecker = (s, l , r) => {
      while (l >= 0 && r < s.length && s[l] === s[r]) {
          console.log(`l is ${l}, r is ${r}, s is ${s}, and s.slice(l, r + 1) is ${s.slice(l, r + 1)}`);
          l--; r++;
      }
      console.log(`l is ${Number(l) + 1} and r is ${Number(r - 1)}`);
      const ans = s.slice(l + 1, r);
      console.log(ans);
      return ans;
  }
  
  let result = '';
  let temp = '';
  
  for (let i in s) {
      console.log('odd checker');
      // for potential odd palindromes
      temp = expandChecker(s, Number(i), Number(i));
      if (temp.length > result.length) {
          result = temp;
      }
      
      console.log('even checker');
      // for potential even palindromes
      temp = expandChecker(s, Number(i), Number(i) + 1);
      if (temp.length > result.length) {
          result = temp;
      }        
  }
  
  return result;
}

// const s = "babad";
const s = 'cbbd';

console.log(longestPalindrome(s));
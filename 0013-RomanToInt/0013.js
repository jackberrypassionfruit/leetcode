const badRomanToInt = (s) => {
  let int = 0;
    let i = 0;
    
    while (i < s.length) {
        if (s[i] === 'M') {int += 1000} 
        
        else if (s[i] === 'D') {int += 500}
        
        else if (s[i] === 'C') {
            if (s[i + 1] && s.slice(i, i + 2) === 'CD') {
                int += 400;
                i++;
            } else if (s[i + 1] && s.slice(i, i + 2) === 'CM') {
                int += 900;
                i++;
            } else {
                int += 100;
            }
        } 
        else if (s[i] == 'L') {int += 50}
        
        else if (s[i] == 'X') {
            if (s[i + 1] && s.slice(i, i + 2) === 'XL') {
                int += 40;
                i++;
            } else if (s[i + 1] && s.slice(i, i + 2) === 'XC'){
                int += 90;
                i++;
            } else {
                int += 10;
            }
        }
        
        else if (s[i] === 'V') {
            int += 5;
        }
        
        else if (s[i] == 'I') {
            if (s[i + 1] && s.slice(i, i + 2) === 'IV') {
                int += 4;
                i++;
            } else if (s[i + 1] && s.slice(i, i + 2) === 'IX') {
                int += 9;
                i++;
            } else {
                int += 1;
            }
        }
        
        
        i++;
    }
    
    
    return int;
}

const romanToInt = (s) => {
  let int = 0;

  romans = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
  }

  for (let i in s) {
    console.log(`first is ${romans[s[i]]} and second is ${romans[s[Number(i) + 1]]}`);
    if (s[Number(i) + 1] && (romans[s[i]] < romans[s[Number(i) + 1]])) {
      int -= romans[s[i]];
    } else {
      int += romans[s[i]];
    }
  }

  return int;
}

console.log(romanToInt("XXIV"))
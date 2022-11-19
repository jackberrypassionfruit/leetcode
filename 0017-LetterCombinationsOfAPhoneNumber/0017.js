const suckyLetterCombinations = digits => {
  numLetters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z']
  }

  digits = digits.split('');

  let letters = digits.map((num) => numLetters[num]);
  console.log('letters: ', letters);

  const letComboHelper = (letters) => {
    // console.log(`letters : ${letters}`);
    if (letters.length > 0) {
      // const result = letters[0].map((lett) => {
      //   const next = letters.slice(1);
      //   // console.log(`lett: ${lett}`);
      //   // console.log(`next: ${next}`);
      //   return lett + letComboHelper(next);
      // });

      return result;
    } else {
      return '';
    }
  }

  // return letters[0];
  return letComboHelper(letters);
}

const letterCombinations = digits => {
  if (digits === undefined || digits.length === 0) {return []};

  numLetters = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
  }

  const res = [];

  const LCHelper = (i, s) => {
    // console.log('s:', s, 'digits[i]: ', digits[i]);
    if (i === digits.length) {
      res.push(s);
      return;
    }
    for (const c of numLetters[digits[i]]) {
      LCHelper(i + 1, s + c);
    }
  }

  LCHelper(0, '');
  return res;
}

console.log(letterCombinations(''));
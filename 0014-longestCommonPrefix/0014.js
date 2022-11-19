const longestCommonPrefix = (strs) => {
    if (!(strs[0])) {
      return '';
    } else if (strs.length === 1) {
      return strs[0];
    }
    let i = 0;
    let a;
    while (strs[0][i]) {
      a = strs[0][i];
      for (let str of strs.slice(1)) {
        if (str[i] != a) {
          return strs[0].slice(0, i);
        }
      }
      i++;
    }

    

    return strs[0].slice(0, i);
};

strs = ["dog", 'doggo'];

console.log(longestCommonPrefix(strs))
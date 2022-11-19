// {({({}){}})()}

// {
//   (
//     {
//       (
//         {

//         }
//       )
//       {

//       }
//     }
//   )
//   (

//   )
// }

const isValid = (s) => {
  let queue = [];

  pairs = {
    '(': ')',
    '{': '}',
    '[': ']'
  }

  for (let bracket of s) {
    // console.log(`queue is ${queue}`);
    // console.log(`bracket is ${bracket}`);
    if (bracket === pairs[queue.slice(-1)]) {
      queue.pop();
    } else if (bracket in pairs) {
      queue.push(bracket);
    } else {
      return false;
    }

  }

  // console.log(queue);
  if (queue.length !== 0) {return false};

  return true;
}

// s = "()"
// s = "()[]{}"
// s = "(]"
s = '{({({}){}})()}'

console.log(isValid(s));
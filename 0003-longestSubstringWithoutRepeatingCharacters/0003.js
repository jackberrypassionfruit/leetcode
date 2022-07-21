let longest_substring = "";
    let current_longest_substring = "";
    
    for (let i = 0; i < s.length; i++)
        {
            current_longest_substring.concat(s[i]);
            
            if (s.slice(0, -1).includes(s.slice(-1)))
                {
                current_longest_substring = ""
                }
            else
                {
                    if (current_longest_substring.length > longest_substring.length)
                        {
                            longest_substring = current_longest_substring;
                        }
                }
            
            
            
        }
    console.log(longest_substring.length);
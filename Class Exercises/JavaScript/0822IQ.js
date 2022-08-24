/* When given two strings from the user, write a function that 
checks if each string is an anagram of the other. 
If yes, return true, otherwise false */

// Take user input

function checkStringsAnagram(a, b) {
    let len1 = a.length;
    let len2 = b.length;
    if(len1 !== len2){
       console.log('Invalid Input');
       return
    }
    let str1 = a.split('').sort().join('');
    let str2 = b.split('').sort().join('');
    if(str1 === str2){
       console.log("True");
    } else { 
       console.log("False");
    }
 }

 checkStringsAnagram("act","cat")

// for(i = 0; i < word1.length; i++)
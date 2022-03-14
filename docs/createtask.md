# Michael Create Task

[Runtime](https://nastyawakened.cf/michael/)

[College Board Requirements](https://apcentral.collegeboard.org/pdf/ap-csp-student-task-directions.pdf?course=ap-computer-science-principles)

### Final Program Code

* Created independenly or collaboratively
* PDF file containing all program code + comments (`# // <!-- --> /*`)
* Code Must Contain
    * Instruction for `input` (user input, device input, data stream, a file)
    * Use of a `list` of data
    * A `prodedure` that contributes the program
    * An `algorithm` that incldues sequencing, selection, and iteration

### A Video - [LOOM VIDEO](https://www.loom.com/share/1bd68515f4c54f4ead04f2b4c6c69500)

* Created independently
* Display the runtime of the program and demonstrates functionality developed by the student
* < 1 minute
* Formats: `.mp4`, `.wmv`, `.mov`
* < 30MB
* PROHIBITED
   * Voice naration
   * Personal Information

### Written Response

* Created independently
* Questions (`3a-3d`)

#### 3a. 
Describe the overall purpose of the program
- The purpose of this program is for a user to be able to guess any word that they want. The program offers default words (colors), but also categories where the user can choose from (classes). Finally, if the user wants to play with another person, the other person can choose a word of their own via an input box.

Describes what functionality of the program is demonstrated in the video
- The functionality of the program is to check the user's guess to the actual word of the program. If it is 1:1 match, the user wins. There are also situations where certain letters of the guess are correct, so the program shows the user the correct letters. Ex: (b l _ _ ) for blue. If the user is completely wrong, the output will just be underscores ( _ ). 

Describes the input and output of the program demonstrated in the video
- The input of the program is buttons as well as the form for guesses. Output is a successful win, or try again. The individual letters for semi-correct guesses is an input as well. 

#### 3b.

##### List:
```js
var category = ['red','blue','green','yellow','orange','purple','pink','brown','cyan','turquoise','magenta'];
var math_cat = ["statistics","calculus","trigonometry","geometry","algebra"];
var science_cat = ["physics","chemistry","biology","astronomy"];
var humanities_cat = ["literature","english","writing","humanities","history","anthropology"];
var electives_cat = ["ceramics","painting","dance","drama"];
```

Identifies the name of the list being used in the response
- The name of one of my lists is category, which is a list of colors for the user to guess. 

Describes what the data contained in the list represent in your program
- The data contained in the list represents the words that the user will guess.

Explains how the selected list manages complexity in your program code by explaining why your program code could not be written, or how it would be written differently, if you did not use the list.
- The list manages complexity because otherwise the words will not be able to randomzie through the list, and the user will end up guessing the same word over and over again. With the list, the program is more complex, but easier to code because I do not have to create multiple variables for each guessing word.

#### 3c.

##### Algorithm:
```js
function guess() {
   var guessW = document.getElementById("guess_word").value; // creates variable for guess (user input)
   // console.log(guessW)
   var splitWord = word.split(''); // turns word into an array (for comparison to guess)
   console.log(splitWord);
   var splitGuess = guessW.split(''); // turns guess into an array (for comparison to the word)
   console.log(splitGuess);
   if (guessW.length == word.length) {
      // https://stackoverflow.com/questions/12433604/how-can-i-find-matching-values-in-two-arrays
      Array.prototype.diff = function(splitWord) {
        var result = [];
        for(var i = 0; i < this.length; i += 1) {
            if(splitWord.indexOf(this[i]) < 0){
                result.push("_");
            } else {
                result.push(this[i]);
            }
        }
        return result;
    };
 console.log(splitWord.diff(splitGuess))
 document.getElementById("space").innerText = splitWord.diff(splitGuess).join(" ");
 document.getElementById("choose").style.display = 'none';
 document.getElementById("subSelect").style.display = 'none';
 if ( guessW == word ) {
     document.getElementById("space").innerHTML = splitWord.join(" ");
     document.getElementById("guess_word").value = ''; // clears input field
     document.getElementById("lives").innerText = "🎉 CONGRATULATIONS! 🎉"; // yay?
     document.getElementById("reload").style.display = 'inline'; // inputs a reload button that reloads the page (effectively resetting the game)
     // hiding inputs/buttons
     var a = ["guessbtn","ff","guess_word","guess_word_label"]
     for ( var i in a ){
         document.getElementById(a[i]).style.display = 'none';
     }
 }  else if ( lives <= 0 ) {
     // alert("Game Over. You stink")
     document.getElementById("guess_word").value = ''; // clears input field
     document.getElementById("reload").style.display = 'inline';
     document.getElementById("lives").innerText = 'Game Over, Try Again.';
     // hiding buttons & inputs
     var b = ["guessbtn","guess_word","guess_word_label"]
     for ( var i in b ){
         document.getElementById(b[i]).style.display = 'none';
         console.log(b[i]);
  }
    } else {
        document.getElementById("guess_word").value = '';
        lives -= 1;
        document.getElementById("lives").innerHTML = "you have " + lives + " lives left";
    } 
   } else {
       document.getElementById("guess_word").value = '';
       document.getElementById("lives").innerHTML = 'Length of Guess has to Match';
   }
}
```

##### Function Call:
```html
<label id='guess_word_label' for="guess_word">Guess the Word</label>
<input style="margin-bottom: 5px;" autocomplete="off" id="guess_word" name="guess_word">
<a class="button" id="guessbtn" onclick="guess()">Guess</a>
```

Describes in general what the identified procedure does and how it contributes to the overall functionality of the program
- My algorithm is the main `guess()` function where it checks the guess to the word, and if it is correct or not outputs are result

Explains in detailed steps how the algorithm implemented in the identified procedure works. Your explanation must be detailed enough for someone else to recreate it.
- The takes the word, and separates the letters in an array. The program then does the same to the guessed word. Then, using a for loop the program checks each index of the word array to the guess array, and depending on whether or not the index is equilvalent, shows an underscore ( _ ) or the actual index ( letter ). I also implemented if statements in the code to show the correct outputs (congrats or try again). 

#### 3d.
Describes two calls to the procedure identified in written response

1st Call:
- If the guess is correct, the program outputs "CONGRATULATIONS" because the user won the game.

2nd Call
- If the guess function is failure, and the user's guess is wrong the function either outputs underscores or letters depending on how close the user's guess was.

Conditions 1st:
- if (word == guess)

Conditions 2nd:
- Whether the index of array #1 is equal to the index of array #2

Result:
- 1st: "🎉 CONGRATULATIONS! 🎉"
- 2nd: "Try Again"


### How My Code Satisfies These Requirements

What is my code? 

[Word Guessing Game](https://github.com/NastyAwakened/NastyAwakened/blob/nastym/michael/templates/michael.html)

Data - array for list of words

```js
var category = ['red','blue','green','yellow','orange','purple','pink','brown','cyan','turquoise','magenta']
var math_cat = ["statistics","calculus","trigonometry","geometry","algebra"];
var science_cat = ["physics","chemistry","biology","astronomy"]
var humanities_cat = []"literature","english","writing","humanities","history","anthropology"]
var electives_cat = ["ceramics","painting","dance","drama"]
var word = ''
```

User Input - Guessing the Word or Choosing a Word

```html
<!-- Guess -->
<label for="guess_word">Guess the Word</label>
<input autocomplete="off" id="guess_word" name="guess_word">
<a class="button" id="guessbtn" onclick="guess()">Guess</a>

<!-- Choose -->
<label for="input_word">Word</label>
<input type="password" id="input_word" name="input_word">
<a class="button" id="inputbtn" onclick="inputWord(); spacesList(0)">Choose!</a>
```

Sequencing - runs code in order

```js
function spacesList() {
    document.getElementById("space").innerHTML = '';
    var spaces = ''
    for (var i = 0; i < word.length; i++) {
        // creating spaces for word length and a life counter
        spaces += "_ ";
        lives += 1
    }
    document.getElementById("space").innerHTML = spaces
    document.getElementById("lives").innerHTML = "You have " + lives + " lives";
    // alert(document.getElementById("space").innerHTML)
}
```

Selection - if `guess` == `word`

```js
if ( guessW == word ) {
    document.getElementById("space").innerHTML = splitWord.join(" ")
    document.getElementById("guess_word").value = ''; // clears input field
    document.getElementById("lives").innerHTML = "CONGRATULATIONS!" // yay?
    document.getElementById("reload").style.display = 'inline' 
}  else if ( lives <= 0 ) {
    document.getElementById("guess_word").value = ''; // clears input field
    document.getElementById("reload").style.display = 'inline'
    document.getElementById("guessbtn").style.display = 'none';
    document.getElementById("lives").innerHTML = 'Game Over, Try Again.'
} else {
    document.getElementById("guess_word").value = ''
    lives -= 1
    document.getElementById("lives").innerHTML = "you have " + lives + " lives left"
} 
```

Iteration - Comparing indexes of arrays for user's guess and the word

```js
Array.prototype.diff = function(splitWord) {
    var result = [];
    for(var i = 0; i < this.length; i += 1) {
        if(splitWord.indexOf(this[i]) < 0){
            result.push("_");
        } else {
            result.push(this[i])
        }
    }
    return result;
};
document.getElementById("space").innerText = splitWord.diff(splitGuess).join(" ")
// splitWord is array for word
// splitGuess is array for guess
```

Return - A Button calls the JavaScript function: `onclick="guess()`

Functions - Several in the code, i.e.: `guess()`, `wordGen()`,`FF()`, `spacesList()`, etc.


// comparaison d'égalité 
// renvoie true  
console.log("hello JS !"); 
let number1 = 123; 
let text1 = "123";  
// comparaison d'égalité 
// renvoie true 
console.log (number1 == text1); 
console.log (text1 == number1);  
// comparaison d'identité
// renvoie false 
console.log (number1 === text1); 
console.log (text1 === number1);

// opérateurs d'incrémentation
console.log(number1)
number1++;
console.log(number1);

//Attention: l'incrémentation se fait après l'affichage.
console.log(number1++);
console.log(number1);

//Solution: l'incrémentation se fait avant l'affigage.
console.log(++number1);

//number1 -= 1
number1--;
console.log(number1);
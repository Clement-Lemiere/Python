// boucle for classique
for(let i = 0; i < 10; i++) {
    console.log("i = " + i);
}

// boucle à rebours
for(let i = 10; i > 0; i--) {
    console.log("i = " + i);
}

//boucle for each
let users= ['foo','bar', 'baz']

// le mot clé "of" permet de récupérer l'élément
for (let user of users) {
    console.log(user);
}

for (let i in users) {
    let user = users[i];
    console.log(`i = ${i}, user = ${user}`);
    //not quote, alt-gr+7
}

users.forEach(
    function(user, i, list){
        console.log(`i = ${i}, user = ${user}`);
    }
);

// syntaxe alternative
users.forEach[
    (user, i, list) => {
        console.log(`i = ${i}, user = ${user}`);
    }
];